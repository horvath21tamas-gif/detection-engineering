import json
import os
from your_module import process_rule  # Cseréld ki a megfelelő importtal

# Segédfüggvény a JSON fájlok betöltésére
def load_json(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} nem található!")
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
    # Generáljunk egy tesztlogot, ha nem találjuk
    log_path = 'test/logs/suspicious_login.json'
    expected_path = 'test/expected/suspicious_login_expected.json'

    # Ha nem léteznek a fájlok, generáljuk le őket
    if not os.path.exists(log_path):
        logs = [
            {
                "EventID": 4624,
                "TargetUserName": "user123",
                "IpAddress": "192.168.1.10",
                "Host": "hostname"
            }
        ]
        with open(log_path, 'w') as f:
            json.dump(logs, f, indent=4)

    if not os.path.exists(expected_path):
        expected = [
            {
                "rule": "Multiple Remote Logons",
                "severity": "medium",
                "technique": "T1021",
                "user": "user123",
                "computer": "hostname"
            }
        ]
        with open(expected_path, 'w') as f:
            json.dump(expected, f, indent=4)

    # Töltsük be a fájlokat és futtassuk a tesztet
    logs = load_json(log_path)
    expected = load_json(expected_path)

    result = process_rule("suspicious_login", logs)

    assert result == expected, f"Detection test failed for suspicious_login. Expected {expected}, got {result}"
