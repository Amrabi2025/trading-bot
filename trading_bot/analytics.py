"""Utility functions for trading analytics."""

from __future__ import annotations


def percentage_change(previous: float, current: float) -> float:
    """Calculate percentage change from previous to current price.

    Args:
        previous: The previous price. Must be non-zero.
        current: The current price.

    Returns:
        The percentage change from previous to current.

    Raises:
        ValueError: If ``previous`` is zero to avoid division by zero.
    """
    if previous == 0:
        raise ValueError("previous price cannot be zero")

    return (current - previous) / previous * 100.0
