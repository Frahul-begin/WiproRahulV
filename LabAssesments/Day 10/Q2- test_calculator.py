import pytest
from calculator import divide

def setup_module():
    print("\n[SETUP] setup_module")

def teardown_module():
    print("\n[TEARDOWN] teardown_module")

def setup_function():
    print("\n[SETUP] setup_function")

def teardown_function():
    print("\n[TEARDOWN] teardown_function")

def test_division_success(numbers):
    a, b = numbers
    assert divide(a, b) == 5

def test_division_by_zero(zero_divisor):
    with pytest.raises(ValueError):
        divide(10, zero_divisor)
