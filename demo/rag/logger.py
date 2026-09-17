"""
Logging module for the Seba Bondhu demo chatbot.

Implements the "reason codes" and "logged access" controls described in
docs/06-ai-risks.md (Explainability) and docs/07-governance-framework.md
(Access controls, Incident response): every interaction is logged with
a structured reason code (answered / escalated / low_confidence), and
the query text is redacted of detected PII BEFORE it is written to
disk — never after. This ordering matters: a log pipeline that redacts
after storage has already created the exposure it was meant to prevent.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from .pii_filter import detect_pii, redact

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
LOG_FILE = os.path.join(LOG_DIR, "queries.jsonl")


def log_interaction(
    raw_query: str,
    reason_code: str,
    doc_id: str | None,
    confidence: float | None,
) -> dict:
    os.makedirs(LOG_DIR, exist_ok=True)
    pii_flags = detect_pii(raw_query)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        # Confidential tier per docs/04-data-classification.md: query text
        # is redacted before it ever touches disk.
        "query_redacted": redact(raw_query),
        "pii_detected": pii_flags,
        "reason_code": reason_code,  # answered | escalated | low_confidence
        "retrieved_doc_id": doc_id,
        "confidence": confidence,
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry
