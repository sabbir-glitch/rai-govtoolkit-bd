"""
PII detection and redaction for the Seba Bondhu demo chatbot.

Implements the mitigation described in docs/05-privacy-risks.md
("Citizens volunteering sensitive data in free-text queries") and
docs/04-data-classification.md (Sensitive tier handling): any NID-like
number or phone number typed into a query is detected and redacted
BEFORE the query is logged. The live query still goes to retrieval
(the user needs their answer), but nothing sensitive should reach
storage in raw form.

This is a deliberately simple, transparent, regex-based implementation
for the demo. A production system would need broader coverage (e.g.
addresses, names) and should treat this as a first line of defence,
not a complete guarantee — that limitation itself should be documented
for anyone extending this toolkit.
"""

from __future__ import annotations

import re

# Bangladeshi NID numbers are commonly 10, 13, or 17 digits.
_NID_PATTERN = re.compile(r"\b\d{10}\b|\b\d{13}\b|\b\d{17}\b")

# Bangladeshi mobile numbers: 01XXXXXXXXX (11 digits) or +8801XXXXXXXXX.
_PHONE_PATTERN = re.compile(r"(\+?880)?01[3-9]\d{8}\b")


def detect_pii(text: str) -> list[str]:
    """Return a list of PII category labels found in the text."""
    found = []
    if _NID_PATTERN.search(text):
        found.append("possible_nid_number")
    if _PHONE_PATTERN.search(text):
        found.append("phone_number")
    return found


def redact(text: str) -> str:
    """Return the text with detected PII replaced by a redaction marker."""
    redacted = _PHONE_PATTERN.sub("[REDACTED_PHONE]", text)
    redacted = _NID_PATTERN.sub("[REDACTED_NID]", redacted)
    return redacted
