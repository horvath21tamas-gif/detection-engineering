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

def evaluate_block(block_data, log):
    if not isinstance(block_data, dict): return False
    
    # Minden kulcs-érték párt ellenőrizni kell a blokkon belül (AND kapcsolat)
    for field_with_modifier, expected_values in block_data.items():
        # Sigma mező tisztítása (pl. Image|contains -> Image)
        clean_field = field_with_modifier.split('|')[0]
        if not isinstance(expected_values, list):
            expected_values = [expected_values]
        
        # Értékek keresése a logban
        found_in_field = False
        
        # 1. Próbáljuk meg közvetlen mezőként (Case-insensitive)
        actual_val = None
        for k, v in log.items():
            if k.lower() == clean_field.lower():
                actual_val = v
                break
        
        if actual_val:
            val_str = str(actual_val).lower()
            if any(str(v).lower().replace('*', '') in val_str for v in expected_values):
                found_in_field = True
        
        # 2. Ha nincs meg, nézzük meg a raw_data-ban (biztonsági háló)
        if not found_in_field and 'raw_data' in log:
            raw_str = str(log['raw_data']).lower()
            if any(str(v).lower().replace('*', '') in raw_str for v in expected_values):
                found_in_field = True
                
        if not found_in_field:
            return False # Ha egy mező sem stimmel a blokkból, a blokk False
            
    return True

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule = yaml.safe_load(f)
    with open(log_path, 'r', encoding='utf-8') as f:
        log = json.load(f)

    detection = rule.get('detection', {})
    condition = detection.get('condition', 'any of selection*').lower()
    
    # Minden detekciós blokk kiértékelése
    results = {k: evaluate_block(v, log) for k, v in detection.items() 
               if k != 'condition' and isinstance(v, dict)}

    # Logikai motor (Egyszerűsített Sigma condition parser)
    if '1 of' in condition or 'any of' in condition:
        matched = any(results.values())
    elif 'all of' in condition:
        matched = all(results.values()) if results else False
    else:
        # Ha konkrét nevek vannak, megnézzük a selection-öket
        matched = any(results.get(k, False) for k in results if 'selection' in k)

    assert matched, f"DETECTION FAILED: {os.path.basename(rule_path)}\nLog: {json.dumps(log, indent=2)}"
