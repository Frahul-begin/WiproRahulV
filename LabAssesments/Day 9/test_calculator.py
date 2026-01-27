import pytest

from calculator import addition, subtract, multiply, divide

def test_addition():
    assert addition(1, 2) == 3

def test_subtraction():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 5) == 15

def test_divisio():
    assert divide(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)