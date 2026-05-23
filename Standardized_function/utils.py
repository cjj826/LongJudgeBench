"""
Shared utility functions for standardization scripts.
"""
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_STANDARDIZED_DIR = BASE_DIR / "data_standardized"
GROUND_TRUTH_DIR = BASE_DIR / "ground_truth"


def ensure_output_dirs():
    """Ensure output directories exist."""
    DATA_STANDARDIZED_DIR.mkdir(parents=True, exist_ok=True)
    GROUND_TRUTH_DIR.mkdir(parents=True, exist_ok=True)


def save_jsonl(data, filepath):
    """Append a record to a JSONL file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")


def clear_jsonl(filepath):
    """Clear a JSONL file (for regeneration)."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("")


def load_jsonl(filepath):
    """Load a JSONL file and return a list of records."""
    if not filepath.exists():
        return []
    data = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def count_tokens(text: str) -> int:
    """Count tokens using tiktoken cl100k_base."""
    if not text:
        return 0
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except ImportError:
        return len(text.split())
