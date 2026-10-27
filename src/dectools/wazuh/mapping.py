"""Loads mapping.yml and resolves a Sigma logsource / field to its Wazuh form."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .logic import KEYWORD_FIELD, Unsupported

DEFAULT_MAPPING = Path(__file__).with_name("mapping.yml")


@dataclass(frozen=True)
class LogSourceProfile:
    field_map: str
    if_sid: tuple[int, ...] = ()
    if_group: str | None = None
    require: tuple[tuple[str, str], ...] = ()
    note: str = ""


@dataclass
class Mapping:
    logsources: list[dict]
    field_maps: dict
    levels: dict
    _cache: dict = field(default_factory=dict, repr=False)

    @classmethod
    def load(cls, path: str | Path | None = None) -> "Mapping":
        data = yaml.safe_load(Path(path or DEFAULT_MAPPING).read_text(encoding="utf-8"))
        return cls(data["logsources"], data["field_maps"], data["levels"])

    def profile_for(self, logsource) -> LogSourceProfile:
        have = {
            "product": (logsource.product or "").lower(),
            "category": (logsource.category or "").lower(),
            "service": (logsource.service or "").lower(),
        }
        for entry in self.logsources:
            match = {k: str(v).lower() for k, v in entry["match"].items()}
            if all(have[k] == v for k, v in match.items()):
                return LogSourceProfile(
                    field_map=entry["field_map"],
                    if_sid=tuple(entry.get("if_sid", ())),
                    if_group=entry.get("if_group"),
                    require=tuple((entry.get("require") or {}).items()),
                    note=entry.get("note", ""),
                )
        desc = "/".join(f"{k}={v}" for k, v in have.items() if v) or "(empty)"
        raise Unsupported(f"unsupported logsource {desc}")

    def wazuh_field(self, profile: LogSourceProfile, sigma_field: str) -> str:
        if sigma_field == KEYWORD_FIELD:
            return KEYWORD_FIELD
        fmap = self.field_maps[profile.field_map]
        # modifiers like Field|contains are already resolved by pySigma
        explicit = fmap.get("map", {})
        if sigma_field in explicit:
            return explicit[sigma_field]
        if fmap["strategy"] == "lower_first" and sigma_field:
            return fmap["prefix"] + sigma_field[0].lower() + sigma_field[1:]
        raise Unsupported(f"field '{sigma_field}' has no Wazuh mapping for {profile.field_map} logs")

    def level(self, sigma_level) -> int:
        name = getattr(sigma_level, "name", None) or "medium"
        return int(self.levels.get(name.lower(), self.levels["medium"]))

    def level_name(self, wazuh_level: int) -> str:
        """Inverse of level(): pick the Sigma level whose Wazuh level is <= wazuh_level."""
        best = "informational"
        for name, lvl in sorted(self.levels.items(), key=lambda kv: kv[1]):
            if lvl <= wazuh_level:
                best = name
        return best
