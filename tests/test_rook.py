"""Tests for Rook piece."""

from __future__ import annotations
import sys

sys.path.append("..")

from core.coordinate import Coordinate
from core.color import Color
from pieces.rook import Rook
from pieces.piece import PieceType, Piece


def test_rook_creation():
    """Test creating a rook."""
    coord = Coordinate.from_str("a1")
    rook = Rook(Color.WHITE, coord)

    assert rook.color == Color.WHITE
    assert rook.coordinate == coord
    assert rook.piece_type == PieceType.ROOK
    assert rook.symbol == "R"  # White rook


def test_rook_empty_board():
    """Test rook movement on empty board."""
    rook = Rook(Color.WHITE, Coordinate.from_str("d4"))
    board_state = {}  # Empty board

    attack_squares = rook.get_attack_squares(board_state)

    # Rook should attack entire rank and file
    expected_squares = {
        # Rank 4 (horizontal)
        Coordinate.from_str("a4"),
        Coordinate.from_str("b4"),
        Coordinate.from_str("c4"),
        Coordinate.from_str("e4"),
        Coordinate.from_str("f4"),
        Coordinate.from_str("g4"),
        Coordinate.from_str("h4"),
        # File d (vertical)
        Coordinate.from_str("d1"),
        Coordinate.from_str("d2"),
        Coordinate.from_str("d3"),
        Coordinate.from_str("d5"),
        Coordinate.from_str("d6"),
        Coordinate.from_str("d7"),
        Coordinate.from_str("d8"),
    }

    assert attack_squares == expected_squares


def test_rook_blocked_by_pieces():
    """Test rook movement blocked by pieces."""
    rook = Rook(Color.WHITE, Coordinate.from_str("d4"))

    # Place blocking pieces
    board_state: dict[Coordinate, Piece] = {
        Coordinate.from_str("d6"): Rook(
            Color.BLACK, Coordinate.from_str("d6")
        ),  # Enemy piece
        Coordinate.from_str("f4"): Rook(
            Color.WHITE, Coordinate.from_str("f4")
        ),  # Friendly piece
    }

    attack_squares = rook.get_attack_squares(board_state)

    # Should attack up to (and including) the enemy piece at d6
    assert Coordinate.from_str("d5") in attack_squares  # One before enemy
    assert Coordinate.from_str("d6") in attack_squares  # Enemy piece itself
    assert Coordinate.from_str("d7") not in attack_squares  # Blocked by enemy
    assert Coordinate.from_str("d8") not in attack_squares  # Blocked by enemy

    # Should attack up to (but not including) friendly piece at f4
    assert Coordinate.from_str("e4") in attack_squares  # One before friendly
    assert (
        Coordinate.from_str("f4") in attack_squares
    )  # Can "attack" friendly (for check detection)
    assert Coordinate.from_str("g4") not in attack_squares  # Blocked by friendly


def test_rook_legal_moves():
    """Test rook legal moves (can't capture own pieces)."""
    rook = Rook(Color.WHITE, Coordinate.from_str("d4"))

    board_state: dict[Coordinate, Piece] = {
        Coordinate.from_str("d6"): Rook(
            Color.BLACK, Coordinate.from_str("d6")
        ),  # Enemy - can capture
        Coordinate.from_str("f4"): Rook(
            Color.WHITE, Coordinate.from_str("f4")
        ),  # Friendly - can't capture
    }

    legal_moves = rook.get_legal_moves(board_state)

    # Can move to empty squares and capture enemy
    assert Coordinate.from_str("d5") in legal_moves  # Empty square
    assert Coordinate.from_str("d6") in legal_moves  # Enemy piece

    # Cannot capture own piece
    assert Coordinate.from_str("f4") not in legal_moves  # Friendly piece


def test_rook_corner_position():
    """Test rook in corner has limited movement."""
    rook = Rook(Color.WHITE, Coordinate.from_str("a1"))
    board_state = {}

    attack_squares = rook.get_attack_squares(board_state)

    # Should only move along rank 1 and file a
    assert len(attack_squares) == 14  # 7 squares on rank + 7 squares on file
    assert Coordinate.from_str("a8") in attack_squares  # Top of file
    assert Coordinate.from_str("h1") in attack_squares  # End of rank


if __name__ == "__main__":
    test_rook_creation()
    test_rook_empty_board()
    test_rook_blocked_by_pieces()
    test_rook_legal_moves()
    test_rook_corner_position()
    print("✅ All rook tests passed!")
