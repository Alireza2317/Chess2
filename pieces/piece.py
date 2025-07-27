"""
Abstract base class for chess pieces.
Defines common interface and behavior for all piece types.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from core.coordinate import Coordinate
from core.color import Color


class PieceType(Enum):
    """Chess piece types."""

    PAWN = "p"
    ROOK = "r"
    KNIGHT = "n"
    BISHOP = "b"
    QUEEN = "q"
    KING = "k"


class Piece(ABC):
    """Abstract base class for all chess pieces."""

    def __init__(self, color: Color, coordinate: Coordinate) -> None:
        self.color = color
        self.coordinate = coordinate
        self.has_moved = False

    @property
    @abstractmethod
    def piece_type(self) -> PieceType:
        """Return the piece type."""
        pass

    @abstractmethod
    def get_attack_squares(
        self, board_state: dict[Coordinate, Piece]
    ) -> set[Coordinate]:
        """
        Get all squares this piece attacks (regardless of occupancy).
        Used for check detection and piece interaction logic.
        """
        pass

    def get_legal_moves(self, board_state: dict[Coordinate, Piece]) -> set[Coordinate]:
        """
        Get all legal moves for this piece.
        Default implementation: attack squares that are empty or
        contain enemy pieces.
        Override for special piece behavior (like pawn).
        """
        legal_moves: set = set()

        for target in self.get_attack_squares(board_state):
            target_piece: Piece | None = board_state.get(target)

            # Can move to empty square or capture enemy piece
            if target_piece is None or target_piece.color != self.color:
                legal_moves.add(target)

        return legal_moves

    @property
    def symbol(self) -> str:
        """Get the piece symbol (uppercase for white, lowercase for black)."""
        symbol: str = self.piece_type.value
        return symbol.upper() if self.color == Color.WHITE else symbol.lower()

    def mark_moved(self) -> None:
        """Mark piece as having moved (for castling, en passant, etc.)."""
        self.has_moved = True

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return f"{self.color} {self.piece_type.name.title()} at {self.coordinate}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Piece):
            return False
        return (
            self.color == other.color
            and self.piece_type == other.piece_type
            and self.coordinate == other.coordinate
        )

    def __hash__(self) -> int:
        return hash(id(self))
