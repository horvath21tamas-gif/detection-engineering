import os
import json
import yaml
import pytest
from sigma.collection import SigmaCollection
from sigma.processing.pipeline import ProcessingPipeline

# Útvonalak a struktúrád alapján
RULES_DIR = 'rules/sigma'
LOGS_DIR = 'test/logs'

def get_test_pairs():
    """Összepárosítja a Sigma szabályokat a generált mock logokkal."""
    test_cases = []
    for root, _, files in os.walk(RULES_DIR):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rule_path = os.path.join(root, file)
                category = os.path.basename(root)
                
                # A generált log neve megegyezik a szabályéval, csak .json
                log_name = file.rsplit('.', 1)[0] + '.json'
                log_path = os.path.join(LOGS_DIR, category, log_name)
                
                if os.path.exists(log_path):
                    test_cases.append((rule_path, log_path))
    return test_cases

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    """Lefuttatja a Sigma logikát a JSON logon."""
    
    # 1. Szabály betöltése
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule_yaml = yaml.safe_load(f)
        # Minimális validáció, hogy ne omoljon össze üres fájlokon
        if not rule_yaml or 'detection' not in rule_yaml:
            pytest.skip(f"Szabály hiányos: {rule_path}")
        
        rule_collection = SigmaCollection.from_yaml(yaml.dump(rule_yaml))

    # 2. Log betöltése
    with open(log_path, 'r', encoding='utf-8') as f:
        mock_log = json.load(f)

    # 3. Illeszkedés vizsgálata
    # A pySigma match() metódusa megnézi, hogy a log esemény elsüti-e a szabályt
    matched = False
    for rule in rule_collection.rules:
        if rule.detection.test_event(mock_log):
            matched = True
            break
    
    assert matched, f"DETEKCIÓS HIBA: A {os.path.basename(rule_path)} szabály nem jelzett a generált logjára ({os.path.basename(log_path)})!"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
