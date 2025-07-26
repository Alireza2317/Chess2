"""
Chess movement directions.
Handles file/rank offsets for piece movement patterns.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import NamedTuple
from core.coordinate import Coordinate


class Direction(NamedTuple):
    """Represents a movement direction with file and rank offsets."""

    file_offset: int
    rank_offset: int

    def apply_to(self, coord: Coordinate) -> Coordinate | None:
        """Apply this direction to a coordinate, return None if off-board."""
        new_file_idx: int = coord.file_index + self.file_offset
        new_rank_idx: int = coord.rank_index + self.rank_offset

        # Check bounds
        if not (0 <= new_file_idx <= 7) or not (0 <= new_rank_idx <= 7):
            return None

        new_file: str = Coordinate.FILES[new_file_idx]
        new_rank: str = Coordinate.RANKS[new_rank_idx]

        return Coordinate(new_file, new_rank)

    def ray_from(self, coord: Coordinate) -> list[Coordinate]:
        """Generate all coordinates in this direction from starting coordinate."""
        coordinates: list[Coordinate] = []
        current: Coordinate = coord

        while True:
            next_coord = self.apply_to(current)
            if next_coord is None:
                break
            coordinates.append(next_coord)
            current = next_coord

        return coordinates


@dataclass(frozen=True)
class Directions:
    """Common chess movement directions."""

    # Orthogonal (rook-like)
    NORTH = Direction(0, 1)
    SOUTH = Direction(0, -1)
    EAST = Direction(1, 0)
    WEST = Direction(-1, 0)

    # Diagonal (bishop-like)
    NORTHEAST = Direction(1, 1)
    NORTHWEST = Direction(-1, 1)
    SOUTHEAST = Direction(1, -1)
    SOUTHWEST = Direction(-1, -1)

    # Knight moves
    KNIGHT_MOVES = [
        Direction(2, 1),
        Direction(2, -1),
        Direction(-2, 1),
        Direction(-2, -1),
        Direction(1, 2),
        Direction(1, -2),
        Direction(-1, 2),
        Direction(-1, -2),
    ]

    # Grouped directions
    ORTHOGONAL = [NORTH, SOUTH, EAST, WEST]
    DIAGONAL = [NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST]
    ALL_EIGHT = ORTHOGONAL + DIAGONAL
