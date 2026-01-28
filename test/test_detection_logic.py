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
    
    # Pre-calculate lower-case raw data for faster searching
    raw_content = str(log.get('raw_data', '')).lower()
    
    for field, expected_values in block_data.items():
        # Handle Sigma modifiers (e.g., field|contains) by taking the prefix
        clean_field = field.split('|')[0].lower()
        if not isinstance(expected_values, list):
            expected_values = [expected_values]
        
        # Check 1: Direct field match in JSON
        found = False
        actual_val = log.get(clean_field)
        if actual_val:
            val_str = str(actual_val).lower()
            if any(str(v).lower().replace('*', '') in val_str for v in expected_values):
                found = True
        
        # Check 2: Fallback - look for the "field: value" pattern inside raw_data
        if not found:
            for v in expected_values:
                search_term = str(v).lower().replace('*', '')
                if search_term in raw_content:
                    found = True
                    break
        
        if not found: return False
    return True

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule = yaml.safe_load(f)
    with open(log_path, 'r', encoding='utf-8') as f:
        log = json.load(f)

    detection = rule.get('detection', {})
    condition = detection.get('condition', 'any of selection*').lower()
    
    # Evaluate all selection blocks
    results = {k: evaluate_block(v, log) for k, v in detection.items() 
               if k != 'condition' and isinstance(v, dict)}

    # Logic Engine
    if '1 of' in condition or 'any of' in condition:
        matched = any(results.values())
    elif 'all of' in condition:
        matched = all(results.values()) if results else False
    else:
        # Default to checking if any 'selection' block is true
        matched = any(results.get(k, False) for k in results if 'selection' in k)

    assert matched, f"DETECTION FAILED: {os.path.basename(rule_path)}\nLog: {json.dumps(log, indent=2)}"
