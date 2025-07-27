"""
Rook chess piece implementation.
Moves horizontally and vertically any number of squares.
"""

from __future__ import annotations
from core.coordinate import Coordinate
from core.direction import Directions
from pieces.piece import Piece, PieceType


class Rook(Piece):
    """Rook piece - moves orthogonally (horizontally and vertically)."""

    @property
    def piece_type(self) -> PieceType:
        return PieceType.ROOK

    def get_attack_squares(
        self, board_state: dict[Coordinate, Piece]
    ) -> set[Coordinate]:
        """Get all squares the rook attacks (orthogonal directions)."""
        attack_squares: set = set()

        # Check all orthogonal directions
        for direction in Directions.ORTHOGONAL:
            # Get all squares in this direction until we hit something
            for target_square in direction.ray_from(self.coordinate):
                attack_squares.add(target_square)

                # Stop if we hit any piece (friendly or enemy)
                if target_square in board_state:
                    break

        return attack_squares
