import pytest
import yaml
import json
import os
import re

def get_test_pairs():
    """
    Összepárosítja a Sigma szabályokat a hozzájuk tartozó JSON log mintákkal.
    Csak azokat a párokat adja vissza, ahol a log fájl létezik.
    """
    pairs = []
    sigma_root = 'rules/sigma'
    log_root = 'test/logs'
    
    if not os.path.exists(sigma_root):
        return pairs

    for root, _, files in os.walk(sigma_root):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rule_path = os.path.join(root, file)
                
                # Relatív útvonal kiszámítása a mappaszerkezet követéséhez
                rel_path = os.path.relpath(root, sigma_root)
                log_name = file.rsplit('.', 1)[0] + '.json'
                log_path = os.path.join(log_root, rel_path, log_name)
                
                if os.path.exists(log_path):
                    pairs.append((rule_path, log_path))
    return pairs

def match_value(expected, actual):
    """
    Alapvető Sigma illesztési logika: támogatja a listákat és a wildcards-okat (*).
    """
    if actual is None:
        return False
    
    actual = str(actual).lower()
    
    if isinstance(expected, list):
        return any(match_value(e, actual) for e in expected)
    
    expected = str(expected).lower()
    
    if '*' in expected:
        # Sigma wildcard átalakítása regex-re
        pattern = re.escape(expected).replace(r'\*', '.*')
        return re.search(f"^{pattern}$", actual) is not None
    
    return expected == actual

def evaluate_block(block, log):
    """
    Kiértékel egy Sigma detekciós blokkot (pl. selection).
    Egy blokkon belül minden mezőnek egyeznie kell (AND logika).
    """
    if not isinstance(block, dict):
        return False
        
    for field_mod, expected_val in block.items():
        # Eltávolítjuk a módosítókat (pl. |contains), csak a mezőnevet nézzük
        field = field_mod.split('|')[0]
        
        # Kis/nagybetű független mezőkeresés a logban
        actual_val = next((v for k, v in log.items() if k.lower() == field.lower()), None)
        
        if not match_value(expected_val, actual_val):
            return False
    return True

@pytest.mark.parametrize("rule_path, log_path", get_test_pairs())
def test_sigma_logic(rule_path, log_path):
    """
    Teszteli a Sigma szabály logikáját egy adott JSON log fájlon.
    """
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule = yaml.safe_load(f)
    with open(log_path, 'r', encoding='utf-8') as f:
        log = json.load(f)

    detection = rule.get('detection', {})
    condition = detection.get('condition', '').lower()
    
    # Minden blokk kiértékelése (kivéve a condition-t)
    results = {
        key: evaluate_block(val, log) 
        for key, val in detection.items() 
        if key != 'condition' and isinstance(val, (dict, list))
    }

    # Egyszerűsített Sigma feltételkezelő
    if not condition or 'any of selection*' in condition:
        matched = any(v for k, v in results.items() if k.startswith('selection'))
    elif 'all of selection*' in condition:
        selections = [v for k, v in results.items() if k.startswith('selection')]
        matched = all(selections) if selections else False
    else:
        # Ha a feltétel konkrét blokkneveket tartalmaz
        matched = any(results.values())

    assert matched, f"DETEKCIÓ SIKERTELEN: {os.path.basename(rule_path)}. A log nem triggerelte a szabályt."
