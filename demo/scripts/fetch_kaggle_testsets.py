"""
Fetch real evaluation datasets from Kaggle to strengthen the demo's test
suite, as catalogued in ../../docs/11-real-data-sources.md.

This is deliberately a download-on-demand script, not a vendored copy of
the data: the datasets belong to their original authors, are versioned
on Kaggle independently of this repo, and one of the four catalogued
sources isn't openly licensed for redistribution at all. Pulling them at
setup time (with the developer's own Kaggle credentials) is the correct
way to depend on external data without duplicating or going stale on it.

Requires the Kaggle CLI and credentials configured — see
https://www.kaggle.com/docs/api. If you don't have Kaggle credentials,
that's fine: the test suite in tests/test_governance_checks.py falls
back to its small built-in dialect sample and skips the real-data tests
gracefully (see test_dialect_testset_if_available).

Usage:
    pip install kaggle
    # place kaggle.json per Kaggle's API docs, or export
    # KAGGLE_USERNAME / KAGGLE_KEY
    python scripts/fetch_kaggle_testsets.py
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

DATASETS = {
    # (kaggle dataset ref, file to extract, license) — see docs/11 for full citation.
    "dialect": ("koushikrudra/bleach-clean-dataset", "cleaned_bangla_test (2).csv", "Apache 2.0"),
    "smishing": ("mdferozahmedafm/bengali-sms-smishing-dataset", None, "MIT"),
}


def _run_kaggle(*args: str) -> None:
    try:
        subprocess.run(["kaggle", *args], check=True)
    except FileNotFoundError:
        print("Kaggle CLI not found. Install it with: pip install kaggle", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Kaggle CLI failed: {e}", file=sys.stderr)
        sys.exit(1)


def fetch_dialect_testset() -> None:
    ref, filename, _ = DATASETS["dialect"]
    target_dir = os.path.join(DATA_DIR, "dialect")
    os.makedirs(target_dir, exist_ok=True)
    print(f"Downloading {filename!r} from {ref} (Apache 2.0)...")
    _run_kaggle("datasets", "download", "-d", ref, "-f", filename, "-p", target_dir, "--unzip")

    # Build a small, de-identified sample JSON the test suite can read,
    # rather than depending directly on Kaggle's CSV column names/order.
    csv_path = os.path.join(target_dir, filename)
    out_path = os.path.join(target_dir, "dialect_testset_sample.json")
    if not os.path.exists(csv_path):
        print(f"Expected file not found after download: {csv_path}", file=sys.stderr)
        return

    samples_by_dialect: dict[str, list[str]] = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dialect = row.get("dialect", "").strip()
            text = row.get("text", "").strip()
            if not dialect or not text:
                continue
            samples_by_dialect.setdefault(dialect, [])
            if len(samples_by_dialect[dialect]) < 5:  # keep it small
                samples_by_dialect[dialect].append(text)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(samples_by_dialect, f, ensure_ascii=False, indent=2)
    print(f"Wrote {sum(len(v) for v in samples_by_dialect.values())} samples "
          f"across {len(samples_by_dialect)} dialects to {out_path}")


def fetch_smishing_dataset() -> None:
    ref, _, _ = DATASETS["smishing"]
    target_dir = os.path.join(DATA_DIR, "smishing")
    os.makedirs(target_dir, exist_ok=True)
    print(f"Downloading full dataset from {ref} (MIT)...")
    _run_kaggle("datasets", "download", "-d", ref, "-p", target_dir, "--unzip")
    print(f"Downloaded to {target_dir} — use the labelled 'smish' rows as "
          f"adversarial test cases for the security-risk checklist item.")


if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    fetch_dialect_testset()
    fetch_smishing_dataset()
    print("\nDone. These files are gitignored — re-run this script on a fresh "
          "clone rather than committing the data.")
