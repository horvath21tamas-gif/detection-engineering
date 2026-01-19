# test/test_rules.py
import pytest
from your_module import process_rule  # Ha más fájlban van a process_rule

def test_process_rule_for_credential_dumping_lsass():
    logs = [
        {
            "TargetImage": "C:\\Windows\\System32\\lsass.exe",
            "Image": "C:\\Tools\\procdump.exe",
            "GrantedAccess": "0x10",
            "User": "user1",
            "Computer": "PC1"
        }
    ]
    result = process_rule("credential_dumping_lsass", logs)
    expected = [{
        "rule": "Credential Dumping LSASS",
        "severity": "high",
        "technique": "T1003.001",
        "user": "user1",
        "computer": "PC1"
    }]
    assert result == expected

def test_process_rule_for_suspicious_login():
    logs = [
        {
            "EventID": 4624,
            "TargetUserName": "user1",
            "IpAddress": "192.168.1.100",
            "Host": "PC1"
        }
    ]
    result = process_rule("suspicious_login", logs)
    expected = [{
        "rule": "Multiple Remote Logons",
        "severity": "medium",
        "technique": "T1021",
        "user": "user1",
        "computer": "PC1"
    }]
    assert result == expected

def test_process_rule_for_unmapped_rule():
    logs = [{"EventID": 9999}]  # Ha nem találunk semmit
    result = process_rule("some_other_rule", logs)
    expected = [{
        "rule": "Rule some_other_rule not matched",
        "severity": "medium",
        "technique": "UNMAPPED"
    }]
    assert result == expected
