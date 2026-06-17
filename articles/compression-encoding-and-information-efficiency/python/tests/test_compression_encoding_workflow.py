from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from compression_encoding.workflow import CompressionEncodingCase, representation_quality, representation_risk
from compression_encoding.examples import run_length_encode, entropy, compression_ratio, checksum, demo_compression_encoding
from calculators.compression_ratio_calculator import compute as compression_compute
from calculators.representation_quality_calculator import compute as quality_compute


def test_representation_scores_in_range():
    case = CompressionEncodingCase("Test", "Context", "Choice", 0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.75, 0.7, 0.8, 0.8)
    assert 0 <= representation_quality(case) <= 100
    assert 0 <= representation_risk(case) <= 100


def test_run_length_and_entropy():
    assert run_length_encode("aaabb") == [("a", 3), ("b", 2)]
    assert entropy("aaaa") == 0.0
    assert entropy("ab") == 1.0


def test_compression_ratio_and_checksum():
    assert compression_ratio(b"abc", b"ab") == 2 / 3
    assert len(checksum(b"abc")) == 64


def test_demo_and_calculators():
    assert "compression_ratio_zlib" in demo_compression_encoding()
    assert "compression_ratio" in compression_compute("aaaaabbbb")
    assert "interpretation" in quality_compute([0.75] * 10)
