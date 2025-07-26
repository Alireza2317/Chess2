"""Tests for Direction class."""

from __future__ import annotations
import sys

sys.path.append("..")

from core.coordinate import Coordinate
from core.direction import Direction, Directions


def test_direction_apply():
    """Test applying direction to coordinate."""
    coord = Coordinate.from_str("e4")

    # Move north
    north = Directions.NORTH.apply_to(coord)
    assert north == Coordinate.from_str("e5")

    # Move northeast
    northeast = Directions.NORTHEAST.apply_to(coord)
    assert northeast == Coordinate.from_str("f5")

    # Move off board
    corner = Coordinate.from_str("h8")
    off_board = Directions.NORTH.apply_to(corner)
    assert off_board is None


def test_direction_ray():
    """Test generating ray in direction."""
    coord = Coordinate.from_str("d4")

    # Ray going east
    east_ray = Directions.EAST.ray_from(coord)
    expected = [
        Coordinate.from_str("e4"),
        Coordinate.from_str("f4"),
        Coordinate.from_str("g4"),
        Coordinate.from_str("h4"),
    ]
    assert east_ray == expected

    # Ray from corner (shorter)
    corner = Coordinate.from_str("g8")
    north_ray = Directions.NORTH.ray_from(corner)
    assert north_ray == []  # Already at top


def test_knight_moves():
    """Test knight move directions."""
    coord = Coordinate.from_str("e4")

    knight_destinations = []
    for direction in Directions.KNIGHT_MOVES:
        dest = direction.apply_to(coord)
        if dest:  # Only valid moves
            knight_destinations.append(dest)

    # Knight from e4 should have 8 valid moves
    assert len(knight_destinations) == 8

    # Check one specific move
    expected_move = Coordinate.from_str("f6")  # Knight move from e4
    assert expected_move in knight_destinations


def test_direction_constants():
    """Test direction constant groups."""
    assert len(Directions.ORTHOGONAL) == 4
    assert len(Directions.DIAGONAL) == 4
    assert len(Directions.ALL_EIGHT) == 8
    assert len(Directions.KNIGHT_MOVES) == 8


if __name__ == "__main__":
    test_direction_apply()
    test_direction_ray()
    test_knight_moves()
    test_direction_constants()
    print("✅ All direction tests passed!")
