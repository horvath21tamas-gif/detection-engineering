# test/test_rule_tests.py

from test.test_rules import process_rule  # Importáld a megfelelő helyről

import json

# Segédfüggvény a JSON fájlok betöltésére
def load_json(path):
    with open(path) as f:
        return json.load(f)

def test_credential_dumping_lsass():
    log_path = 'test/logs/credential_dumping_lsass.json'
    expected_path = 'test/expected/credential_dumping_lsass_expected.json'

    logs = load_json(log_path)
    expected = load_json(expected_path)

    result = process_rule("credential_dumping_lsass", logs)

    assert result == expected, f"Detection test failed for credential_dumping_lsass. Expected {expected}, got {result}"

def test_suspicious_login():
    log_path = 'test/logs/suspicious_login.json'
    expected_path = 'test/expected/suspicious_login_expected.json'

    logs = load_json(log_path)
    expected = load_json(expected_path)

    result = process_rule("suspicious_login", logs)

    assert result == expected, f"Detection test failed for suspicious_login. Expected {expected}, got {result}"
