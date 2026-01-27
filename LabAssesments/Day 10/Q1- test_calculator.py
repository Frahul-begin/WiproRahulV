import pytest
from calculator import divide

def test_division():
    assert divide(20, 4) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(20, 0)