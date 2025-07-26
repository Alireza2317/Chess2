"""Tests for Color enum."""

import sys

sys.path.append("..")

from core.color import Color


def test_color_opposite():
    """Test color opposite functionality."""
    assert Color.WHITE.opposite() == Color.BLACK
    assert Color.BLACK.opposite() == Color.WHITE

    # Test ~ operator
    assert ~Color.WHITE == Color.BLACK
    assert ~Color.BLACK == Color.WHITE


def test_color_string():
    """Test string representation."""
    assert str(Color.WHITE) == "White"
    assert str(Color.BLACK) == "Black"
    assert Color.WHITE.name_title == "White"


if __name__ == "__main__":
    test_color_opposite()
    test_color_string()
    print("✅ All color tests passed!")
