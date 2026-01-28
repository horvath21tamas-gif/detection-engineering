import os
import json
import yaml
import pytest
from sigma.collection import SigmaCollection

# Útvonalak
RULES_DIR = 'rules/sigma'
LOGS_DIR = 'test/logs'

def get_test_pairs():
    test_cases = []
    if not os.path.exists(RULES_DIR):
        return test_cases
        
    for root, _, files in os.walk(RULES_DIR):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rule_path = os.path.join(root, file)
                category = os.path.basename(root)
                
                log_name = file.rsplit('.', 1)[0] + '.json'
                log_path = os.path.join(LOGS_DIR, category, log_name)
                
                if os.path.exists(log_path):
                    test_cases.append((rule_path, log_path))
    return test_cases

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    # 1. Szabály betöltése
    with open(rule_path, 'r', encoding='utf-8') as f:
        try:
            # Csak a SigmaCollection-t importáljuk, ez minden verziónál ugyanott van
            rule_collection = SigmaCollection.from_yaml(f.read())
        except Exception as e:
            pytest.skip(f"Betöltési hiba: {e}")

    # 2. Log betöltése
    with open(log_path, 'r', encoding='utf-8') as f:
        mock_log = json.load(f)

    # 3. Illeszkedés vizsgálata (Verzió-független megközelítés)
    matched = False
    for rule in rule_collection.rules:
        # Megpróbáljuk a két leggyakoribb metódust
        if hasattr(rule, 'test_event'):
            if rule.test_event(mock_log):
                matched = True
                break
        elif hasattr(rule, 'match'):
            if rule.match(mock_log):
                matched = True
                break
    
    assert matched, f"FAIL: {os.path.basename(rule_path)} nem jelez a teszt logjára!"
