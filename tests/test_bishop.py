"""Tests for Bishop piece."""

from __future__ import annotations
import sys

sys.path.append("..")

from core.coordinate import Coordinate
from core.color import Color
from pieces.bishop import Bishop
from pieces.piece import Piece, PieceType


def test_bishop_creation():
    """Test creating a bishop."""
    coord = Coordinate.from_str("c1")
    bishop = Bishop(Color.WHITE, coord)

    assert bishop.color == Color.WHITE
    assert bishop.coordinate == coord
    assert bishop.piece_type == PieceType.BISHOP
    assert bishop.symbol == "B"  # White bishop


def test_bishop_empty_board():
    """Test bishop movement on empty board."""
    bishop = Bishop(Color.WHITE, Coordinate.from_str("d4"))
    board_state = {}  # Empty board

    attack_squares = bishop.get_attack_squares(board_state)

    # Bishop should attack all diagonal squares
    expected_squares = {
        # Northeast diagonal
        Coordinate.from_str("e5"),
        Coordinate.from_str("f6"),
        Coordinate.from_str("g7"),
        Coordinate.from_str("h8"),
        # Northwest diagonal
        Coordinate.from_str("c5"),
        Coordinate.from_str("b6"),
        Coordinate.from_str("a7"),
        # Southeast diagonal
        Coordinate.from_str("e3"),
        Coordinate.from_str("f2"),
        Coordinate.from_str("g1"),
        # Southwest diagonal
        Coordinate.from_str("c3"),
        Coordinate.from_str("b2"),
        Coordinate.from_str("a1"),
    }

    assert attack_squares == expected_squares


def test_bishop_blocked_by_pieces():
    """Test bishop movement blocked by pieces."""
    bishop = Bishop(Color.WHITE, Coordinate.from_str("d4"))

    # Place blocking pieces
    board_state: dict[Coordinate, Piece] = {
        Coordinate.from_str("f6"): Bishop(
            Color.BLACK, Coordinate.from_str("f6")
        ),  # Enemy piece
        Coordinate.from_str("b2"): Bishop(
            Color.WHITE, Coordinate.from_str("b2")
        ),  # Friendly piece
    }

    attack_squares = bishop.get_attack_squares(board_state)

    # Should attack up to (and including) the enemy piece at f6
    assert Coordinate.from_str("e5") in attack_squares  # One before enemy
    assert Coordinate.from_str("f6") in attack_squares  # Enemy piece itself
    assert Coordinate.from_str("g7") not in attack_squares  # Blocked by enemy
    assert Coordinate.from_str("h8") not in attack_squares  # Blocked by enemy

    # Should attack up to (and including) friendly piece at b2
    assert Coordinate.from_str("c3") in attack_squares  # One before friendly
    assert (
        Coordinate.from_str("b2") in attack_squares
    )  # Can "attack" friendly (for check detection)
    assert Coordinate.from_str("a1") not in attack_squares  # Blocked by friendly


def test_bishop_legal_moves():
    """Test bishop legal moves (can't capture own pieces)."""
    bishop = Bishop(Color.WHITE, Coordinate.from_str("d4"))

    board_state: dict[Coordinate, Piece] = {
        Coordinate.from_str("f6"): Bishop(
            Color.BLACK, Coordinate.from_str("f6")
        ),  # Enemy - can capture
        Coordinate.from_str("b2"): Bishop(
            Color.WHITE, Coordinate.from_str("b2")
        ),  # Friendly - can't capture
    }

    legal_moves = bishop.get_legal_moves(board_state)

    # Can move to empty squares and capture enemy
    assert Coordinate.from_str("e5") in legal_moves  # Empty square
    assert Coordinate.from_str("f6") in legal_moves  # Enemy piece

    # Cannot capture own piece
    assert Coordinate.from_str("b2") not in legal_moves  # Friendly piece


def test_bishop_corner_position():
    """Test bishop in corner has limited movement."""
    bishop = Bishop(Color.WHITE, Coordinate.from_str("a1"))
    board_state = {}

    attack_squares = bishop.get_attack_squares(board_state)

    # Should only move along one diagonal from corner
    expected = {
        Coordinate.from_str("b2"),
        Coordinate.from_str("c3"),
        Coordinate.from_str("d4"),
        Coordinate.from_str("e5"),
        Coordinate.from_str("f6"),
        Coordinate.from_str("g7"),
        Coordinate.from_str("h8"),
    }

    assert attack_squares == expected
    assert len(attack_squares) == 7  # Only one diagonal available


def test_bishop_center_vs_corner():
    """Test bishop has more squares available in center."""
    # Center bishop
    center_bishop = Bishop(Color.WHITE, Coordinate.from_str("d4"))
    center_attacks = center_bishop.get_attack_squares({})

    # Corner bishop
    corner_bishop = Bishop(Color.WHITE, Coordinate.from_str("a1"))
    corner_attacks = corner_bishop.get_attack_squares({})

    # Center should have more attack squares
    assert len(center_attacks) > len(corner_attacks)
    assert len(center_attacks) == 13  # 4 diagonals with varying lengths
    assert len(corner_attacks) == 7  # Only 1 diagonal


if __name__ == "__main__":
    test_bishop_creation()
    test_bishop_empty_board()
    test_bishop_blocked_by_pieces()
    test_bishop_legal_moves()
    test_bishop_corner_position()
    test_bishop_center_vs_corner()
    print("✅ All bishop tests passed!")
