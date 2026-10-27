"""Integration test of wazuh-deploy-gate with a fake Wazuh (fake binaries + fake logtest API)."""

import json
import os
import stat
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

from dectools.wazuh import cli
from dectools.wazuh.convert import build_ruleset
from dectools.wazuh.registry import IdRegistry

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "wazuh" / "server" / "wazuh-deploy-gate"

RULE = """title: WMIC remote
id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c7777
status: test
description: d
author: t
date: 2026-01-01
level: critical
tags: [attack.execution, attack.t1047]
logsource: {product: windows, category: process_creation}
detection:
  sel:
    Image|endswith: '\\\\wmic.exe'
    CommandLine|contains: '/node:'
  condition: sel
"""


class FakeWazuh:
    """Evaluates logtest requests with dectools' own matcher."""

    def __init__(self, rules_dir: Path, mapping):
        self.rules_dir, self.mapping = rules_dir, mapping
        self.broken = False
        handler = self._handler()
        self.httpd = HTTPServer(("127.0.0.1", 0), handler)
        self.port = self.httpd.server_address[1]
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def _loaded_rules(self):
        from lxml import etree

        from dectools.wazuh.cli import main as _  # noqa: F401  (import side effects only)
        from dectools.wazuh.emit import FieldReq, WazuhRule

        rules = []
        for f in sorted(self.rules_dir.glob("sigma_*.xml")):
            for r in etree.parse(str(f)).getroot().iter("rule"):
                reqs = [FieldReq(e.get("name"), e.text, e.get("negate") == "yes") for e in r.iter("field")]
                rules.append(WazuhRule(int(r.get("id")), int(r.get("level")), "", requirements=reqs))
        return rules

    def _handler(self):
        outer = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _send(self, payload, raw=False):
                body = payload.encode() if raw else json.dumps(payload).encode()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(body)

            def do_POST(self):
                self._send("fake-jwt", raw=True)

            def do_PUT(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                from dectools.wazuh.matcher import rule_matches

                flat = {}

                def walk(prefix, node):
                    for k, v in node.items():
                        (walk(f"{prefix}{k}.", v) if isinstance(v, dict) else flat.__setitem__(f"{prefix}{k}", v))

                walk("", json.loads(body["event"]))
                hit = None
                if not outer.broken:
                    for r in outer._loaded_rules():
                        if rule_matches(r, flat):
                            hit = r
                            break
                out = {"rule": {"id": str(hit.id), "level": hit.level}} if hit else {}
                self._send({"data": {"token": "t", "output": out}})

        return H


@pytest.fixture
def lab(tmp_path, mapping):
    rules_src = tmp_path / "src"
    rules_src.mkdir()
    (rules_src / "T1047.yml").write_text(RULE)
    build = tmp_path / "build"
    assert cli.main(["build", "--rules", str(rules_src), "--out", str(build), "--registry", str(tmp_path / "reg.json"), "--update-registry"]) == 0
    benign = tmp_path / "benign.jsonl"
    benign.write_text((ROOT / "wazuh" / "benign_events.jsonl").read_text())
    bundle = tmp_path / "bundle.tar.gz"
    assert cli.main(["bundle", "--build", str(build), "--benign", str(benign), "--out", str(bundle), "--git-sha", "abc123"]) == 0

    rules_dir, state = tmp_path / "etc-rules", tmp_path / "state"
    rules_dir.mkdir()
    (rules_dir / "local_rules.xml").write_text("<group name='local'></group>")
    fake = FakeWazuh(rules_dir, mapping)
    bindir = tmp_path / "bin"
    bindir.mkdir()
    for name, rc in (("analysisd", 0), ("restart", 0)):
        p = bindir / name
        p.write_text(f"#!/bin/sh\nif [ -f '{tmp_path}/fail-{name}' ]; then echo boom >&2; exit 1; fi\nexit {rc}\n")
        p.chmod(p.stat().st_mode | stat.S_IEXEC)
    env_file = tmp_path / "api.env"
    env_file.write_text(f"WAZUH_API_URL=http://127.0.0.1:{fake.port}\nWAZUH_API_USER=u\nWAZUH_API_PASSWORD=p\n")
    env = {
        **os.environ,
        "WDG_RULES_DIR": str(rules_dir), "WDG_STATE_DIR": str(state), "WDG_ANALYSISD": str(bindir / "analysisd"),
        "WDG_RESTART_CMD": str(bindir / "restart"), "WDG_API_ENV_FILE": str(env_file), "WDG_FILE_GROUP": "root",
    }
    return {"tmp": tmp_path, "bundle": bundle, "rules_dir": rules_dir, "state": state, "env": env, "fake": fake}


def gate(lab, command: str, bundle: Path | None = None):
    data = command.encode() + b"\n" + (bundle.read_bytes() if bundle else b"")
    p = subprocess.run([sys.executable, str(GATE)], input=data, capture_output=True, env=lab["env"], timeout=120)
    lines = [json.loads(line) for line in p.stdout.decode().splitlines() if line.startswith("{")]
    return p.returncode, lines


def stages(lines):
    return [x["stage"] for x in lines]


def test_successful_deploy(lab):
    rc, lines = gate(lab, "deploy", lab["bundle"])
    assert rc == 0, lines
    assert stages(lines)[-1] == "done"
    assert (lab["rules_dir"] / "sigma_1_critical.xml").exists()
    assert (lab["rules_dir"] / "local_rules.xml").exists()  # foreign files untouched
    logtest = next(x for x in lines if x["stage"] == "logtest")
    assert logtest["attack_fired"] == logtest["attack_vectors"] == 1 and logtest["benign_false_positives"] == []
    rc, lines = gate(lab, "status")
    assert rc == 0 and lines[0]["git_sha"] == "abc123"


def test_syntax_failure_rolls_back(lab):
    gate(lab, "deploy", lab["bundle"])  # establish a good state
    before = (lab["rules_dir"] / "sigma_1_critical.xml").read_text()
    (lab["rules_dir"] / "sigma_1_critical.xml").write_text("<group name='old'/>")  # pretend older version
    (lab["tmp"] / "fail-analysisd").write_text("x")
    rc, lines = gate(lab, "deploy", lab["bundle"])
    assert rc == 1 and "failure" in stages(lines)
    assert (lab["rules_dir"] / "sigma_1_critical.xml").read_text() == "<group name='old'/>"
    assert before != "<group name='old'/>"


def test_logtest_failure_rolls_back_and_removes_new_files(lab):
    lab["fake"].broken = True  # nothing fires -> attack vectors missed
    rc, lines = gate(lab, "deploy", lab["bundle"])
    assert rc == 1
    assert not list(lab["rules_dir"].glob("sigma_*.xml"))  # back to the (empty) previous state
    assert any(x["stage"] == "rollback" and x["ok"] for x in lines)


def test_tampered_bundle_is_rejected(lab, tmp_path):
    import io
    import tarfile

    data = lab["bundle"].read_bytes()
    out = io.BytesIO()
    with tarfile.open(fileobj=io.BytesIO(data)) as src, tarfile.open(fileobj=out, mode="w:gz") as dst:
        for m in src.getmembers():
            payload = src.extractfile(m).read()
            if m.name.startswith("rules/"):
                payload += b"<!-- tampered -->"
                m.size = len(payload)
            dst.addfile(m, io.BytesIO(payload))
    bad = tmp_path / "bad.tar.gz"
    bad.write_bytes(out.getvalue())
    rc, lines = gate(lab, "deploy", bad)
    assert rc == 1 and "hash mismatch" in lines[-1]["error"]
    assert not list(lab["rules_dir"].glob("sigma_*.xml"))


def test_path_traversal_and_foreign_files_rejected(lab, tmp_path):
    import io
    import tarfile

    out = io.BytesIO()
    with tarfile.open(fileobj=out, mode="w:gz") as tf:
        info = tarfile.TarInfo("../../etc/passwd")
        info.size = 1
        tf.addfile(info, io.BytesIO(b"x"))
    evil = tmp_path / "evil.tar.gz"
    evil.write_bytes(out.getvalue())
    rc, lines = gate(lab, "deploy", evil)
    assert rc == 1 and "unsafe" in lines[-1]["error"]


def test_rollback_command(lab):
    gate(lab, "deploy", lab["bundle"])
    gate(lab, "deploy", lab["bundle"])  # second deploy creates a backup holding v1
    rc, lines = gate(lab, "rollback")
    assert rc == 0 and lines[-1]["stage"] == "rollback"


def test_unknown_command(lab):
    rc, lines = gate(lab, "rm -rf /")
    assert rc == 1 and "unknown command" in lines[-1]["error"]


def test_benign_events_do_not_trigger_any_repo_rule(mapping):
    root = ROOT / "rules" / "sigma"
    if not root.exists():
        pytest.skip("no rules")
    quarantine = cli.load_quarantine(str(ROOT / "wazuh" / "quarantine.yml"))
    res = build_ruleset(root, mapping, IdRegistry(), quarantine=quarantine)
    rules = [r for o in res.outcomes for r in o.rules]
    from dectools.wazuh.matcher import rule_matches

    for line in (ROOT / "wazuh" / "benign_events.jsonl").read_text().splitlines():
        row = json.loads(line)
        flat = cli.flatten(json.loads(row["log"]))
        hits = [r for r in rules if rule_matches(r, flat)]
        assert not hits, f"benign event '{row['name']}' triggers {[(h.id, h.description) for h in hits][:3]}"
