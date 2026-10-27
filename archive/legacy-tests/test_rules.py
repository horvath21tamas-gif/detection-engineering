import sys
import os

# Ez a rész megmondja a Pythonnak, hogy nézzen be a tools mappába is modulokért
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tools'))

import pytest
import yaml
# Most már nem fog hibát dobni az importálásnál
from validate_metadata import validate_rule_metadata

# Példa a validálás tesztelésére
def test_validate_metadata_valid():
    # Hozz létre egy ideiglenes teszt fájlt
    test_file = 'test_rule.yaml'
    with open(test_file, 'w') as file:
        yaml.dump({
            'id': 'test-id',
            'title': 'Test Rule',
            'description': 'This is a test rule'
        }, file)
    
    # Teszteld a validálást
    result = validate_rule_metadata(test_file)
    assert result is True, f"Expected True but got {result}"
    
    # Töröld a teszt fájlt
    os.remove(test_file)

def test_validate_metadata_invalid():
    # Hozz létre egy hibás teszt fájlt (hiányzó mezők)
    test_file = 'invalid_rule.yaml'
    with open(test_file, 'w') as file:
        yaml.dump({
            'id': 'test-id',
            # Hiányzik a 'title' és 'description'
        }, file)
    
    # Teszteld a validálást
    result = validate_rule_metadata(test_file)
    assert result is False, f"Expected False but got {result}"
    
    # Töröld a teszt fájlt
    os.remove(test_file)
