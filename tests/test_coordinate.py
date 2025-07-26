"""Tests for Coordinate class."""

import sys

sys.path.append("..")

from core.coordinate import Coordinate


def test_coordinate_creation():
    """Test creating coordinates."""
    coord = Coordinate("e", "4")
    assert coord.file == "e"
    assert coord.rank == "4"
    assert str(coord) == "<e4>"


def test_coordinate_from_string():
    """Test creating from string."""
    coord = Coordinate.from_str("a1")
    assert coord.file == "a"
    assert coord.rank == "1"


def test_coordinate_indices():
    """Test index calculations."""
    coord = Coordinate.from_str("a1")
    assert coord.file_index == 0
    assert coord.rank_index == 0
    assert coord.array_indices == (7, 0)  # Bottom-left in array

    coord = Coordinate.from_str("h8")
    assert coord.file_index == 7
    assert coord.rank_index == 7
    assert coord.array_indices == (0, 7)  # Top-right in array


def test_coordinate_equality():
    """Test coordinate comparison."""
    coord1 = Coordinate("e", "4")
    coord2 = Coordinate.from_str("e4")
    coord3 = Coordinate("d", "4")

    assert coord1 == coord2
    assert coord1 != coord3
    assert coord1 != "e4"  # Different type


def test_invalid_coordinates():
    """Test invalid coordinate handling."""
    try:
        Coordinate("z", "1")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    try:
        Coordinate.from_str("e9")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


if __name__ == "__main__":
    test_coordinate_creation()
    test_coordinate_from_string()
    test_coordinate_indices()
    test_coordinate_equality()
    test_invalid_coordinates()
    print("✅ All coordinate tests passed!")
