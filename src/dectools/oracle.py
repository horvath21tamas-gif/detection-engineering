"""Reference evaluator for Sigma conditions on a flat event dict.

Independent of every SIEM translation: it walks the pySigma condition tree and
matches values with its own wildcard matcher. Used to test rules ("this event must
/ must not trigger") and as the oracle in the Wazuh differential tests.
Field lookup is case-insensitive; a missing field behaves like an empty value.
"""

from __future__ import annotations

import ipaddress
import re

from sigma.conditions import (
    ConditionAND,
    ConditionFieldEqualsValueExpression,
    ConditionNOT,
    ConditionOR,
    ConditionValueExpression,
)
from sigma.types import (
    SigmaCasedString,
    SigmaCIDRExpression,
    SigmaNull,
    SigmaNumber,
    SigmaRegularExpression,
    SigmaString,
    SpecialChars,
)

from .wazuh.logic import KEYWORD_FIELD, Unsupported


def glob_match(parts, text, cased):
    if not cased:
        text = text.lower()

    def lit(p):
        return str(p) if cased else str(p).lower()

    def rec(i, j):
        if i == len(parts):
            return j == len(text)
        p = parts[i]
        if p is SpecialChars.WILDCARD_MULTI:
            return any(rec(i + 1, k) for k in range(j, len(text) + 1))
        if p is SpecialChars.WILDCARD_SINGLE:
            return j < len(text) and rec(i + 1, j + 1)
        s = lit(p)
        return text.startswith(s, j) and rec(i + 1, j + len(s))

    return rec(0, 0)


def match_value(value, actual):
    if isinstance(value, SigmaString):
        return glob_match(value.s, str(actual), isinstance(value, SigmaCasedString))
    if isinstance(value, SigmaNull):
        return str(actual) == ""
    if isinstance(value, SigmaNumber):
        return str(actual) == str(value.number)
    if isinstance(value, SigmaRegularExpression):
        flags = 0
        names = {f.name for f in value.flags}
        flags |= re.I if "IGNORECASE" in names else 0
        flags |= re.S if "DOTALL" in names else 0
        flags |= re.M if "MULTILINE" in names else 0
        return re.search(str(value.regexp), str(actual), flags) is not None
    if isinstance(value, SigmaCIDRExpression):
        try:
            return ipaddress.ip_address(str(actual)) in value.network
        except ValueError:
            return False
    raise Unsupported(type(value).__name__)


def evaluate(node, event):
    if isinstance(node, ConditionAND):
        return all(evaluate(a, event) for a in node.args)
    if isinstance(node, ConditionOR):
        return any(evaluate(a, event) for a in node.args)
    if isinstance(node, ConditionNOT):
        return not evaluate(node.args[0], event)
    if isinstance(node, ConditionFieldEqualsValueExpression):
        return match_value(node.value, _get(event, node.field))
    if isinstance(node, ConditionValueExpression):
        return match_value(node.value, _get(event, KEYWORD_FIELD))
    raise AssertionError(node)


def leaves(node):
    if isinstance(node, (ConditionAND, ConditionOR, ConditionNOT)):
        for a in node.args:
            yield from leaves(a)
    else:
        yield node


def _get(event, field):
    if field in event:
        return event[field]
    lowered = {k.lower(): v for k, v in event.items()}
    return lowered.get(field.lower(), "")


def rule_triggers(rule, event) -> bool:
    """True if any condition of the pySigma rule matches the event."""
    return any(evaluate(c.parsed, event) for c in rule.detection.parsed_condition)
