"""
Chess board squares.
Represents individual squares with their color and coordinate.
"""

from __future__ import annotations
from core.coordinate import Coordinate
from core.color import Color


class Square:
    """Represents a single square on a chess board."""

    def __init__(self, coordinate: Coordinate) -> None:
        self.coordinate: Coordinate = coordinate
        self.color: Color = self._calculate_color()

    def _calculate_color(self) -> Color:
        """Calculate square color based on coordinate."""
        file_idx: int = self.coordinate.file_index
        rank_idx: int = self.coordinate.rank_index

        # Square is white if file + rank indices sum to odd number
        return Color.WHITE if (file_idx + rank_idx) % 2 == 1 else Color.BLACK

    def __str__(self) -> str:
        return str(self.coordinate)

    def __repr__(self) -> str:
        return f"Square({self.coordinate}, {self.color})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Square):
            return False
        return self.coordinate == other.coordinate

    def __hash__(self) -> int:
        return hash(self.coordinate)
