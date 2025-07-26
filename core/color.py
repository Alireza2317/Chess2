"""
Chess piece and square colors.
Simple enum with toggle functionality.
"""

import enum


class Color(enum.Enum):
    """Represents piece color and square color in chess."""

    WHITE = 1
    BLACK = -1

    def opposite(self) -> "Color":
        """Return the opposite color."""
        return Color.WHITE if self == Color.BLACK else Color.BLACK

    def __invert__(self) -> "Color":
        """Enable ~color syntax for getting opposite color."""
        return self.opposite()

    @property
    def name_title(self) -> str:
        """Return capitalized color name."""
        return self.name.title()

    def __str__(self) -> str:
        return self.name_title
