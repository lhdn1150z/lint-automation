import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from clean import multiply, is_even  # noqa: E402


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
