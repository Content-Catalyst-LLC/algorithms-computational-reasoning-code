from __future__ import annotations

import csv
import hashlib
import math
import zlib
from pathlib import Path


def run_length_encode(text: str) -> list[tuple[str, int]]:
    if not text:
        return []
    encoded: list[tuple[str, int]] = []
    current = text[0]
    count = 1
    for character in text[1:]:
        if character == current:
            count += 1
        else:
            encoded.append((current, count))
            current = character
            count = 1
    encoded.append((current, count))
    return encoded


def entropy(text: str) -> float:
    if not text:
        return 0.0
    counts: dict[str, int] = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    total = len(text)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def compression_ratio(original: bytes, compressed: bytes) -> float:
    if len(original) == 0:
        return 1.0
    return len(compressed) / len(original)


def checksum(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def load_sample_text(article_root: Path | None = None) -> str:
    default = "aaaaabbbbccccccccddddeeeeeeeee"
    if article_root is None:
        return default
    path = article_root / "data" / "synthetic_encoding_samples.csv"
    if not path.exists():
        return default
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("use_case") == "run_length_demo":
                return row["sample_text"]
    return default


def demo_compression_encoding(article_root: Path | None = None) -> dict[str, object]:
    text = load_sample_text(article_root)
    original = text.encode("utf-8")
    compressed = zlib.compress(original)
    return {
        "sample_text": text,
        "run_length_encoding": run_length_encode(text),
        "entropy_bits_per_symbol": round(entropy(text), 4),
        "original_bytes": len(original),
        "compressed_bytes_zlib": len(compressed),
        "compression_ratio_zlib": round(compression_ratio(original, compressed), 4),
        "sha256_checksum": checksum(original),
        "interpretation": "Compression uses repeated structure, but small examples may not compress well after format overhead; integrity checks help detect change.",
    }
