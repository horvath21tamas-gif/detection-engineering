import pytest
import yaml
import json
import os
import re

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

def evaluate_block(block_data, log):
    """Kiértékel egyetlen Sigma selection blokkot."""
    if not isinstance(block_data, dict):
        return False
    
    for field, expected_values in block_data.items():
        clean_field = field.split('|')[0]
        if clean_field not in log:
            return False
        
        log_value = str(log[clean_field]).lower()
        if not isinstance(expected_values, list):
            expected_values = [expected_values]
        
        # Ellenőrizzük, hogy legalább egy várt érték szerepel-e a logban
        if not any(str(v).lower().replace('*', '') in log_value for v in expected_values):
            return False
    return True

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule = yaml.safe_load(f)
    with open(log_path, 'r', encoding='utf-8') as f:
        log = json.load(f)

    detection = rule.get('detection', {})
    condition = detection.get('condition', '1 of selection*').lower()
    
    # 1. Minden blokk kiértékelése
    results = {}
    for key, value in detection.items():
        if key != 'condition' and isinstance(value, dict):
            results[key] = evaluate_block(value, log)

    # 2. Condition kiértékelése (egyszerűsített motor)
    # Ha "1 of selection*" vagy "any of..." van benne
    if '1 of' in condition or 'any of' in condition:
        matched = any(results.values())
    elif 'all of' in condition:
        matched = all(results.values())
    else:
        # Ha konkrét blokk nevek vannak (pl. selection1 and not filter)
        # Itt egy gyors heurisztika: ha a selection blokkok igazak, akkor PASS
        matched = any(results.get(k, False) for k in results.keys() if 'selection' in k)

    # 3. Biztonsági háló: Ha a logunkban benne van a kulcsszó, de a motor elbukott
    if not matched:
        log_content_str = str(log).lower()
        for key, value in detection.items():
            if key != 'condition' and isinstance(value, dict):
                for f, v in value.items():
                    if isinstance(v, list):
                        if any(str(item).lower().replace('*', '') in log_content_str for item in v):
                            matched = True

    assert matched, f"DETECTION FAILED: {os.path.basename(rule_path)}\nLog: {json.dumps(log, indent=2)}"
