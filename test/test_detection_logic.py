import pytest
import yaml
import json
import os

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
    # Szabály betöltése
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule = yaml.safe_load(f)
    
    # Log betöltése
    with open(log_path, 'r', encoding='utf-8') as f:
        log = json.load(f)

    detection = rule.get('detection', {})
    condition = detection.get('condition', '').lower()
    
    # Keressük meg a selection blokkokat
    found_match = False
    
    # Egyszerűsített logika: ha a log bármelyik kulcs-érték párja 
    # szerepel a szabály valamelyik definíciójában, akkor érvényesnek vesszük
    for block_name, block_data in detection.items():
        if block_name == 'condition' or not isinstance(block_data, dict):
            continue
            
        block_match = True
        for field, expected_values in block_data.items():
            clean_field = field.split('|')[0]
            
            # Ha a mező nincs a logban, ez a blokk nem egyezik
            if clean_field not in log:
                block_match = False
                break
            
            log_value = str(log[clean_field]).lower()
            
            # Listakezelés
            if not isinstance(expected_values, list):
                expected_values = [expected_values]
            
            # Érték ellenőrzése (tartalmazza-e)
            if not any(str(v).lower().replace('*', '') in log_value for v in expected_values):
                block_match = False
                break
        
        if block_match:
            found_match = True
            break

    assert found_match, f"A log nem felel meg a szabály kritériumainak: {os.path.basename(rule_path)}"
