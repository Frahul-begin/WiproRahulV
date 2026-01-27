import pytest

@pytest.fixture()
def setup_teardown():
    print("Setting up")
    yield
    print("teardown")

def test_example(setup_teardown):
    print("test running")

def test_example1(setup_teardown):
    print("test2 running")

