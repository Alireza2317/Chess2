"""
Chess board coordinates.
Handles file-rank notation (a1, h8) and validation.
"""

from __future__ import annotations
from typing import Self


class Coordinate:
    """Represents a chess board coordinate like 'e4' or 'a1'."""

    FILES: str = "abcdefgh"
    RANKS: str = "12345678"

    def __init__(self, file: str, rank: str) -> None:
        if not self._is_valid(file, rank):
            raise ValueError(f"Invalid coordinate: {file}{rank}")

        self.file: str = file
        self.rank: str = rank

    @classmethod
    def from_str(cls, coord_str: str) -> Self:
        """Create coordinate from string like 'e4'."""
        if len(coord_str) != 2:
            raise ValueError(f"Coordinate string must be 2 characters: {coord_str}")

        return cls(*coord_str)

    @classmethod
    def _is_valid(cls, file: str, rank: str) -> bool:
        """Check if file and rank are valid."""
        return (
            isinstance(file, str)
            and isinstance(rank, str)
            and file in cls.FILES
            and rank in cls.RANKS
        )

    @property
    def file_index(self) -> int:
        """Get file as 0-7 index (a=0, h=7)."""
        return self.FILES.index(self.file)

    @property
    def rank_index(self) -> int:
        """Get rank as 0-7 index (1=0, 8=7)."""
        return self.RANKS.index(self.rank)

    @property
    def array_indices(self) -> tuple[int, int]:
        """Get (row, col) for 2D array access."""
        row = 7 - self.rank_index  # Flip for display (rank 8 = row 0)
        col = self.file_index
        return (row, col)

    def __str__(self) -> str:
        return f"<{self.file}{self.rank}>"

    def __repr__(self) -> str:
        return f"Coordinate('{self}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return False
        return self.file == other.file and self.rank == other.rank

    def __hash__(self) -> int:
        return hash((self.file, self.rank))
