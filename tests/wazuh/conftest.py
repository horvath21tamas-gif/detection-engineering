import textwrap

import pytest
from sigma.collection import SigmaCollection

from dectools.wazuh.convert import convert_sigma_rule
from dectools.wazuh.mapping import Mapping
from dectools.wazuh.registry import IdRegistry


@pytest.fixture(scope="session")
def mapping():
    return Mapping.load()


@pytest.fixture
def compile_rule(mapping):
    """compile_rule(yaml_text) -> list[WazuhRule]"""

    def _compile(yaml_text: str):
        rule = SigmaCollection.from_yaml(textwrap.dedent(yaml_text)).rules[0]
        return convert_sigma_rule(rule, mapping, IdRegistry())

    return _compile


HEADER = """
title: Test rule
id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c1111
status: test
level: high
tags: [attack.execution, attack.t1059.001]
logsource: {{product: windows, category: process_creation}}
detection:
{body}
"""


@pytest.fixture
def sigma():
    def _make(body: str) -> str:
        indented = "\n".join("  " + line for line in textwrap.dedent(body).strip().splitlines())
        return HEADER.format(body=indented)

    return _make
