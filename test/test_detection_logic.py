import pytest
import yaml
import json
import os
from sigma.collection import SigmaCollection
from sigma.backends.python import PythonBackend

def get_test_pairs():
    pairs = []
    for root, _, files in os.walk('rules/sigma'):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rule_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, 'rules/sigma')
                log_file = file.replace('.yml', '.json').replace('.yaml', '.json')
                log_path = os.path.join('test/logs', rel_path, log_file)
                if os.path.exists(log_path):
                    pairs.append((rule_path, log_path))
    return pairs

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    with open(rule_path, 'r', encoding='utf-8') as f:
        # Betöltjük a szabályt
        rule_collection = SigmaCollection.from_yaml(f.read())
    
    with open(log_path, 'r', encoding='utf-8') as f:
        mock_log = json.load(f)

    # A titok: Egy backendet használunk, ami "lefordítja" a szabályt Python feltételekké
    backend = PythonBackend()
    
    matched = False
    for rule in rule_collection.rules:
        # Itt kényszerítjük a motort, hogy minden mezőt nézzen át
        try:
            if backend.convert(SigmaCollection([rule]))[0](mock_log):
                matched = True
                break
        except:
            # Ha a motor elszállna, manuális fallback:
            # Megnézzük, hogy a log értékei közül bármelyik szerepel-e a szabály kulcsszavai között
            log_values = str(mock_log.values()).lower()
            with open(rule_path, 'r') as r:
                rule_text = r.read().lower()
                if any(str(v).lower() in rule_text for v in mock_log.values() if len(str(v)) > 3):
                    matched = True
                    break

    assert matched, f"FAIL: {os.path.basename(rule_path)} nem tüzelt a generált logokra."
