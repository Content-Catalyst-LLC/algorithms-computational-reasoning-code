#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import zlib
from pathlib import Path
from compression_encoding.examples import entropy, checksum


def compute(text: str) -> dict[str, float | int | str]:
    original = text.encode("utf-8")
    compressed = zlib.compress(original)
    ratio = len(compressed) / len(original) if original else 1.0
    return {
        "original_bytes": len(original),
        "compressed_bytes_zlib": len(compressed),
        "compression_ratio": round(ratio, 4),
        "space_saved_percent": round((1 - ratio) * 100, 2),
        "entropy_bits_per_symbol": round(entropy(text), 4),
        "sha256_checksum": checksum(original),
        "interpretation": "Small strings can compress poorly because compressed formats include overhead; compression improves when repeated structure is large enough.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compression ratio, entropy, and checksum calculator.")
    parser.add_argument("--text", default="aaaaabbbbccccccccddddeeeeeeeee")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    result = compute(args.text)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "compression_ratio_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
