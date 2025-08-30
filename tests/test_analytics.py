import os
import sys
import pytest

# Ensure package root is on path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from trading_bot.analytics import percentage_change


def test_percentage_change_positive():
    assert percentage_change(100, 110) == 10.0


def test_percentage_change_zero_previous():
    with pytest.raises(ValueError):
        percentage_change(0, 110)
