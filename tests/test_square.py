"""Tests for Square class."""

from __future__ import annotations
import sys

sys.path.append("..")

from core.coordinate import Coordinate
from core.square import Square
from core.color import Color


def test_square_creation():
    """Test creating squares."""
    coord = Coordinate.from_str("e4")
    square = Square(coord)

    assert square.coordinate == coord
    assert str(square) == "<e4>"


def test_square_colors():
    """Test square color calculation."""
    light_squares = ["h7", "e4", "h1", "a2"]
    for coord_str in light_squares:
        square = Square(Coordinate.from_str(coord_str))
        assert square.color == Color.WHITE, f"{coord_str} should be light"

    dark_squares = ["b2", "e5", "h8", "a1", "a3"]
    for coord_str in dark_squares:
        square = Square(Coordinate.from_str(coord_str))
        assert square.color == Color.BLACK, f"{coord_str} should be dark"


def test_square_equality():
    """Test square comparison."""
    coord1 = Coordinate.from_str("e4")
    coord2 = Coordinate.from_str("e4")
    coord3 = Coordinate.from_str("d4")

    square1 = Square(coord1)
    square2 = Square(coord2)
    square3 = Square(coord3)

    assert square1 == square2  # Same coordinate
    assert square1 != square3  # Different coordinate
    assert square1 != "e4"  # Different type


def test_square_hash():
    """Test square can be used in sets/dicts."""
    squares = {
        Square(Coordinate.from_str("e4")),
        Square(Coordinate.from_str("e4")),  # Duplicate
        Square(Coordinate.from_str("d4")),
    }

    # Should only have 2 unique squares
    assert len(squares) == 2


def test_corner_squares():
    """Test the four corner squares."""
    corners = {
        "a1": False,
        "a8": True,
        "h1": True,
        "h8": False,
    }

    for coord_str, should_be_light in corners.items():
        square = Square(Coordinate.from_str(coord_str))
        if should_be_light:
            assert square.color == Color.WHITE, f"{coord_str} should be light"
        else:
            assert square.color == Color.BLACK, f"{coord_str} should be dark"


if __name__ == "__main__":
    test_square_creation()
    test_square_colors()
    test_square_equality()
    test_square_hash()
    test_corner_squares()
    print("✅ All square tests passed!")
