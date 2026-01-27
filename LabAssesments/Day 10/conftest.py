import pytest

@pytest.fixture(scope="function")
def numbers():
    return 10, 2


@pytest.fixture(scope="module")
def zero_divisor():
    print("\n[SETUP] Module-level fixture")
    yield 0
    print("\n[TEARDOWN] Module-level fixture")
