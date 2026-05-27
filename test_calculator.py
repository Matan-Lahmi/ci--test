import pytest
from calculator import add, divide, multiply, power, subtract


def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(10, 5) == 2
    assert divide(-10, 2) == -5

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_power():
    assert power(2, 8) == 256
    assert power(5, 0) == 1
    assert power(9, 0.5) == 3
