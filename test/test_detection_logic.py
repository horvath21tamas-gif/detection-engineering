import yaml
import pytest

def simulate_log(rule_logic, log_data):
    """Egyszerűsített szimulátor, ami ellenőrzi, hogy a log illeszkedik-e a szabályra."""
    # Ez egy alap példa, a valóságban a Sigma-cli-t vagy egy log-matchert hívunk meg
    selection = rule_logic.get('detection', {}).get('selection', {})
    for key, value in selection.items():
        if log_data.get(key) != value:
            return False
    return True

def test_lsass_dump_rule():
    # Példa egy konkrét szabály tesztelésére
    with open('rules/sigma/credential_access/credential_dumping_lsass.yml', 'r') as f:
        rule = yaml.safe_load(f)
    
    mock_log = {
        'Image': 'C:\\Windows\\System32\\procdump.exe',
        'CommandLine': '-ma lsass.exe'
    }
    
    assert simulate_log(rule, mock_log) == True
