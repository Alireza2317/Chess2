"""Tests for Piece base class."""

from __future__ import annotations
import sys

sys.path.append("..")

from core.coordinate import Coordinate
from core.color import Color
from pieces.piece import Piece, PieceType


# Create a concrete piece for testing
class TestPiece(Piece):
    """Test piece implementation."""

    @property
    def piece_type(self) -> PieceType:
        return PieceType.PAWN

    def get_attack_squares(
        self, board_state: dict[Coordinate, Piece]
    ) -> set[Coordinate]:
        # Simple test: just return one square ahead
        return {Coordinate.from_str("e5")}


def test_piece_creation():
    """Test creating a piece."""
    coord = Coordinate.from_str("e4")
    piece = TestPiece(Color.WHITE, coord)

    assert piece.color == Color.WHITE
    assert piece.coordinate == coord
    assert piece.piece_type == PieceType.PAWN
    assert not piece.has_moved


def test_piece_symbol():
    """Test piece symbol generation."""
    coord = Coordinate.from_str("e4")

    white_piece = TestPiece(Color.WHITE, coord)
    assert white_piece.symbol == "P"  # Uppercase for white

    black_piece = TestPiece(Color.BLACK, coord)
    assert black_piece.symbol == "p"  # Lowercase for black


def test_piece_moved():
    """Test piece movement tracking."""
    piece = TestPiece(Color.WHITE, Coordinate.from_str("e4"))

    assert not piece.has_moved
    piece.mark_moved()
    assert piece.has_moved


def test_piece_equality():
    """Test piece comparison."""
    coord1 = Coordinate.from_str("e4")
    coord2 = Coordinate.from_str("d4")

    piece1 = TestPiece(Color.WHITE, coord1)
    piece2 = TestPiece(Color.WHITE, coord1)  # Same
    piece3 = TestPiece(Color.BLACK, coord1)  # Different color
    piece4 = TestPiece(Color.WHITE, coord2)  # Different position

    assert piece1 == piece2
    assert piece1 != piece3
    assert piece1 != piece4


def test_legal_moves_basic():
    """Test basic legal move generation."""
    piece = TestPiece(Color.WHITE, Coordinate.from_str("e4"))

    # Empty board - should be able to move to attack square
    board_state = {}
    legal_moves = piece.get_legal_moves(board_state)
    assert Coordinate.from_str("e5") in legal_moves


if __name__ == "__main__":
    test_piece_creation()
    test_piece_symbol()
    test_piece_moved()
    test_piece_equality()
    test_legal_moves_basic()
    print("✅ All piece base tests passed!")
