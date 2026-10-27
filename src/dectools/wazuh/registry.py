"""Stable Wazuh rule-id allocation.

Wazuh rule ids must never change for a given detection, otherwise alert history,
dashboards and tuning (overwrite rules) break. The registry file is committed to
git and maps ``<sigma-uuid>:<clause-hash>`` to an integer id. Ids are handed out
sequentially and are never reused, even after a rule is deleted.
"""

from __future__ import annotations

import json
from pathlib import Path

DEFAULT_BASE = 100000
DEFAULT_MAX = 119999  # Wazuh reserves 100000-120000 for user rules


class RegistryFull(Exception):
    pass


class IdRegistry:
    def __init__(self, data: dict | None = None, base: int = DEFAULT_BASE, max_id: int = DEFAULT_MAX):
        data = data or {}
        self.base = int(data.get("base", base))
        self.max_id = int(data.get("max_id", max_id))
        self.next_id = int(data.get("next_id", self.base))
        self.assigned: dict[str, int] = dict(data.get("assigned", {}))
        self.retired: dict[str, int] = dict(data.get("retired", {}))
        self._seen: set[str] = set()
        self._dirty = False

    @classmethod
    def load(cls, path: str | Path, **kwargs) -> "IdRegistry":
        p = Path(path)
        if p.exists():
            return cls(json.loads(p.read_text(encoding="utf-8")))
        return cls(**kwargs)

    def get(self, key: str) -> int:
        self._seen.add(key)
        if key in self.assigned:
            return self.assigned[key]
        if key in self.retired:  # a rule came back: give it its old id again
            self.assigned[key] = self.retired.pop(key)
            self._dirty = True
            return self.assigned[key]
        if self.next_id > self.max_id:
            raise RegistryFull(f"no free Wazuh rule ids left in {self.base}-{self.max_id}")
        self.assigned[key] = self.next_id
        self.next_id += 1
        self._dirty = True
        return self.assigned[key]

    def retire_unseen(self) -> None:
        """Call after a *full* build only."""
        for key in sorted(set(self.assigned) - self._seen):
            self.retired[key] = self.assigned.pop(key)
            self._dirty = True

    @property
    def dirty(self) -> bool:
        return self._dirty

    def to_json(self) -> str:
        return json.dumps(
            {
                "base": self.base,
                "max_id": self.max_id,
                "next_id": self.next_id,
                "assigned": dict(sorted(self.assigned.items(), key=lambda kv: kv[1])),
                "retired": dict(sorted(self.retired.items(), key=lambda kv: kv[1])),
            },
            indent=1,
            ensure_ascii=False,
        ) + "\n"

    def save(self, path: str | Path) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(self.to_json(), encoding="utf-8")
