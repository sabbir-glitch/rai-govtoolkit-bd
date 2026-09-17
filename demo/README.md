# Seba Bondhu — Demo Chatbot

A small, runnable implementation of the governance principles in `../docs/`. This is **not** a production system — it's a working demonstration that the mitigations described in the toolkit are actually implementable, not just aspirational text.

## What this demonstrates, and where

| Governance principle | Where it's implemented |
|---|---|
| Retrieval-grounded answers, never open-ended generation | `rag/retriever.py` — TF-IDF retrieval over `knowledge_base/*.md`; `app.py` only ever returns text from a retrieved document |
| Explicit "not certain" fallback to a human channel | `rag/retriever.py` `CONFIDENCE_THRESHOLD` + `app.py` `HUMAN_ESCALATION_MESSAGE` |
| No eligibility determinations (scope boundary) | `app.py` `ELIGIBILITY_GUARD_PHRASES` intercepts eligibility questions before returning a bare answer |
| PII detection and redaction before logging | `rag/pii_filter.py`, applied inside `rag/logger.py` before any write to disk |
| Reason-coded, explainable logging | `rag/logger.py` — every interaction logged with `answered` / `escalated` / `low_confidence` / `eligibility_boundary` |
| Dialect/robustness testing as an automated check | `tests/test_governance_checks.py::test_informal_low_literacy_phrasing_still_retrieves_correct_document` |
| Off-topic / adversarial query handling | `tests/test_governance_checks.py::test_low_confidence_query_would_trigger_fallback` |

## Setup

```bash
cd demo
python -m venv venv && source venv/bin/activate   # optional but recommended
pip install -r requirements.txt
```

## Run the chatbot

```bash
python app.py
```

Try questions like:
- "How do I correct my date of birth on my NID?"
- "What documents do I need for a trade licence?"
- "Am I eligible for the old age allowance?" — notice it explains criteria but won't say yes/no.
- "What's the weather today?" — notice it escalates instead of guessing.

Type `quit` to exit.

## Run the tests

```bash
pytest tests/ -v
```

These aren't just unit tests — several of them are automated versions of specific items in `../docs/08-responsible-ai-checklist.md`. That's deliberate: a checklist that's only ever reviewed manually tends to lapse; the ones that can be automated, are.

## Inspect the logs

After running the chatbot, check `logs/queries.jsonl` — you'll see that any NID-like number or phone number you typed was redacted **before** it was written, matching the "Sensitive tier" handling rule in `../docs/04-data-classification.md`.

## Optional: real data instead of illustrative samples

Two catalogued real datasets (see `../docs/11-real-data-sources.md`) can strengthen this demo's test suite beyond the small hand-written samples:

```bash
pip install kaggle
# configure Kaggle credentials: https://www.kaggle.com/docs/api
python scripts/fetch_kaggle_testsets.py
```

This downloads a real 10-dialect Bangla corpus and a real Bengali SMS smishing (phishing) dataset into `data/` (gitignored — re-run on a fresh clone rather than committing the data). Once fetched, `pytest tests/ -v` picks up `test_dialect_testset_if_available` automatically instead of skipping it. The smishing dataset isn't wired into an automated test here, but its labelled `smish` rows are exactly what a real adversarial-input test for the Security checklist item (`08-responsible-ai-checklist.md`) should be built from.

## Known limitations (intentional, for a demo)

- TF-IDF retrieval is simple and English-stopword-aware only; a production system would need proper Bangla NLP handling (this is flagged, not hidden — see `../docs/06-ai-risks.md` Bias section for why that matters).
- The PII filter catches NID- and phone-number-shaped patterns only; it does not catch names, addresses, or more subtle identifiers. Treat it as a first line of defence, not a complete guarantee — anyone extending this should read `rag/pii_filter.py`'s docstring before assuming broader coverage.
- Knowledge-base content is illustrative, not verified against current official circulars — every document says so explicitly and should not be used as real guidance.
- No actual SMS/WhatsApp channel, no real human-escalation queue — both are out of scope for this demo but represent real integration work for a pilot.
