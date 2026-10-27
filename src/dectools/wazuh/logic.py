"""Sigma condition tree -> Wazuh-friendly disjunctive normal form (DNF).

A Wazuh rule is a conjunction (AND) of requirements.  OR across *different*
fields cannot be expressed in a single rule, so every Sigma rule is turned
into a DNF: a list of clauses, one Wazuh rule per clause.

To keep the number of clauses small, OR over several values of the *same*
field (the usual Sigma value list) is folded into one atom that later becomes
a single regex alternation.
"""

from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass, field
from itertools import product

from sigma.conditions import (
    ConditionAND,
    ConditionFieldEqualsValueExpression,
    ConditionNOT,
    ConditionOR,
    ConditionValueExpression,
)
from sigma.types import (
    SigmaBool,
    SigmaCasedString,
    SigmaCIDRExpression,
    SigmaCompareExpression,
    SigmaExists,
    SigmaFieldReference,
    SigmaNull,
    SigmaNumber,
    SigmaRegularExpression,
    SigmaString,
    SpecialChars,
)

KEYWORD_FIELD = "<keyword>"  # pseudo field: whole log line (Wazuh full_log)
MAX_CLAUSES = 64


class Unsupported(Exception):
    """The rule (or a part of it) cannot be expressed as a Wazuh rule."""


@dataclass(frozen=True)
class Pat:
    """One regex fragment.

    prefix/suffix say whether the fragment is anchored at the start/end of the
    field value.  ``body`` is a PCRE2 fragment without anchors or flags.
    """

    body: str
    prefix: bool = False
    suffix: bool = False
    cased: bool = False
    sample: str | None = field(default=None, compare=False)  # a literal that matches (for test vectors)

    def standalone(self) -> str:
        rx = ("^" if self.prefix else "") + self.body + ("$" if self.suffix else "")
        return f"(?-i:{rx})" if self.cased else rx

    def lookahead(self) -> str:
        rx = ("" if self.prefix else ".*?") + self.body + ("$" if self.suffix else "")
        inner = f"(?-i:{rx})" if self.cased else rx
        return f"(?={inner})"


@dataclass(frozen=True)
class Atom:
    """field matches ANY of ``alts`` (neg=False) or NONE of them (neg=True)."""

    field: str
    alts: tuple[Pat, ...]
    neg: bool = False


def _esc(text: str) -> str:
    """PCRE2-escape a literal. Spaces become \\x20 so XML trimming cannot eat them."""
    out = []
    for ch in text:
        if ch == " ":
            out.append(r"\x20")
        elif ch == "\n":
            out.append(r"\n")
        elif ch == "\r":
            out.append(r"\r")
        elif ch == "\t":
            out.append(r"\t")
        elif re.match(r"[A-Za-z0-9_]", ch) or ord(ch) > 127:
            out.append(ch)
        else:
            out.append("\\" + ch)
    return "".join(out)


def _string_pat(value: SigmaString, cased: bool) -> Pat:
    parts = list(value.s)
    prefix = not (parts and parts[0] is SpecialChars.WILDCARD_MULTI)
    suffix = not (parts and parts[-1] is SpecialChars.WILDCARD_MULTI)
    if not prefix:
        parts = parts[1:]
    if not suffix and parts:
        parts = parts[:-1]
    body, sample = [], []
    for part in parts:
        if part is SpecialChars.WILDCARD_MULTI:
            body.append(".*")
            sample.append("x")
        elif part is SpecialChars.WILDCARD_SINGLE:
            body.append(".")
            sample.append("z")
        else:
            body.append(_esc(str(part)))
            sample.append(str(part))
    return Pat("".join(body), prefix, suffix, cased, "".join(sample))


def _cidr_pat(value: SigmaCIDRExpression) -> Pat:
    net = value.network
    if not isinstance(net, ipaddress.IPv4Network) or net.prefixlen % 8 != 0:
        raise Unsupported(f"CIDR {value.cidr} is not octet-aligned (/8,/16,/24,/32)")
    octets = str(net.network_address).split(".")[: net.prefixlen // 8]
    host = str(net[1] if net.num_addresses > 1 else net.network_address)
    if not octets:
        return Pat(r"\d+\.\d+\.\d+\.\d+", True, True, False, host)
    if net.prefixlen < 32:
        return Pat(r"\.".join(octets) + r"\.", True, False, False, host)
    return Pat(r"\.".join(octets), True, True, False, host)


def _leaf_atom(field: str, value, neg: bool) -> Atom:
    if isinstance(value, SigmaCasedString):
        return Atom(field, (_string_pat(value, True),), neg)
    if isinstance(value, SigmaString):
        return Atom(field, (_string_pat(value, False),), neg)
    if isinstance(value, SigmaNumber):
        return Atom(field, (Pat(_esc(str(value.number)), True, True, False, str(value.number)),), neg)
    if isinstance(value, SigmaBool):
        return Atom(field, (Pat("true" if value.boolean else "false", True, True, False, "true" if value.boolean else "false"),), neg)
    if isinstance(value, SigmaRegularExpression):
        flags = {str(getattr(f, "name", f)).lower() for f in value.flags}
        body = str(value.regexp)
        if "ignorecase" in flags:
            pat = Pat(body, False, False, False)
        else:
            pat = Pat(body, False, False, True)
        if "dotall" in flags:
            pat = Pat(f"(?s:{pat.body})", False, False, pat.cased)
        if "multiline" in flags:
            pat = Pat(f"(?m:{pat.body})", False, False, pat.cased)
        return Atom(field, (pat,), neg)
    if isinstance(value, SigmaCIDRExpression):
        return Atom(field, (_cidr_pat(value),), neg)
    if isinstance(value, SigmaNull):
        if neg:  # NOT field==null  ->  field exists / non-empty
            return Atom(field, (Pat(".+", False, False),), False)
        raise Unsupported(f"'{field}: null' (absent field) cannot be matched in Wazuh")
    if isinstance(value, SigmaExists):
        if value.exists != neg:  # exists:true (pos) / exists:false (neg)
            return Atom(field, (Pat(".+", False, False),), False)
        raise Unsupported(f"'{field}|exists: false' cannot be matched in Wazuh")
    if isinstance(value, SigmaCompareExpression):
        raise Unsupported(f"numeric comparison on '{field}' is not supported")
    if isinstance(value, SigmaFieldReference):
        raise Unsupported(f"field reference ('fieldref') on '{field}' is not supported")
    raise Unsupported(f"value type {type(value).__name__} on '{field}' is not supported")


# --- tree handling ----------------------------------------------------------
# Nodes after normalisation: Atom | ("and", [nodes]) | ("or", [nodes])


def _nnf(node, neg: bool = False):
    """Negation normal form: NOT only on leaves (folded into Atom.neg)."""
    if isinstance(node, ConditionNOT):
        return _nnf(node.args[0], not neg)
    if isinstance(node, ConditionAND):
        kind = "or" if neg else "and"
        return (kind, [_nnf(a, neg) for a in node.args])
    if isinstance(node, ConditionOR):
        kind = "and" if neg else "or"
        return (kind, [_nnf(a, neg) for a in node.args])
    if isinstance(node, ConditionFieldEqualsValueExpression):
        return _leaf_atom(node.field, node.value, neg)
    if isinstance(node, ConditionValueExpression):
        return _leaf_atom(KEYWORD_FIELD, node.value, neg)
    raise Unsupported(f"unexpected condition node {type(node).__name__}")


def _merge(node):
    """Fold OR of positive same-field atoms and AND of negative same-field atoms."""
    if isinstance(node, Atom):
        return node
    kind, args = node
    args = [_merge(a) for a in args]
    # flatten nested same-kind nodes
    flat = []
    for a in args:
        if isinstance(a, tuple) and a[0] == kind:
            flat.extend(a[1])
        else:
            flat.append(a)
    foldable_neg = kind == "and"  # AND of NOT(...) == NOT(any of ...)
    by_field: dict[str, Atom] = {}
    rest = []
    for a in flat:
        if isinstance(a, Atom) and a.neg == foldable_neg:
            prev = by_field.get(a.field)
            by_field[a.field] = (
                a if prev is None else Atom(a.field, _dedup(prev.alts + a.alts), a.neg)
            )
        else:
            rest.append(a)
    merged = list(by_field.values()) + rest
    return merged[0] if len(merged) == 1 else (kind, merged)


def _dedup(alts):
    seen, out = set(), []
    for a in alts:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return tuple(out)


def _dnf(node):
    """Return list of frozenset[Atom]."""
    if isinstance(node, Atom):
        return [frozenset([node])]
    kind, args = node
    parts = [_dnf(a) for a in args]
    if kind == "or":
        out = [c for p in parts for c in p]
    else:
        total = 1
        for p in parts:
            total *= len(p)
            if total > MAX_CLAUSES * 4:
                raise Unsupported(f"condition expands to more than {MAX_CLAUSES} Wazuh rules")
        out = [frozenset().union(*combo) for combo in product(*parts)]
    # drop duplicates and clauses that are supersets of another clause
    uniq = []
    for c in out:
        if c not in uniq:
            uniq.append(c)
    uniq.sort(key=len)
    kept: list[frozenset] = []
    for c in uniq:
        if not any(k <= c for k in kept):
            kept.append(c)
    if len(kept) > MAX_CLAUSES:
        raise Unsupported(f"condition expands to {len(kept)} Wazuh rules (limit {MAX_CLAUSES})")
    return kept


def condition_to_dnf(parsed_condition) -> list[frozenset[Atom]]:
    return _dnf(_merge(_nnf(parsed_condition)))


def canonical_clause(clause: frozenset[Atom]) -> str:
    """Stable text form of a clause, used to derive rule-id registry keys."""
    items = sorted(
        (a.field, a.neg, tuple(sorted(p.standalone() for p in a.alts))) for a in clause
    )
    return repr(items)
