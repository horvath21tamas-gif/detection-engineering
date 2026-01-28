import pytest
import yaml
import json
import os
from sigma.collection import SigmaCollection

def get_test_pairs():
    pairs = []
    rule_base = 'rules/sigma'
    log_base = 'test/logs'
    for root, _, files in os.walk(rule_base):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rel_path = os.path.relpath(root, rule_base)
                rule_path = os.path.join(root, file)
                log_path = os.path.join(log_base, rel_path, file.rsplit('.', 1)[0] + '.json')
                if os.path.exists(log_path):
                    pairs.append((rule_path, log_path))
    return pairs

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule_collection = SigmaCollection.from_yaml(f.read())

    with open(log_path, 'r', encoding='utf-8') as f:
        mock_log = json.load(f)

    matched = False
    for rule in rule_collection.rules:
        # Sigma motor specifikus tesztelés
        try:
            if rule.test_event(mock_log):
                matched = True
                break
        except Exception:
            # Ha a test_event nem elérhető, próbáljuk a match-et
            if hasattr(rule, 'match') and rule.match(mock_log):
                matched = True
                break

    # Részletes hibaüzenet, ha elbukik
    assert matched, f"DETECTION FAILED!\nRule: {os.path.basename(rule_path)}\nLog Content: {json.dumps(mock_log, indent=2)}"
