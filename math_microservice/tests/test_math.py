import pytest
from app.services import math_service

def test_pow_op():
    assert math_service.pow_op(2, 3) == 8
    assert math_service.pow_op(5, 0) == 1
    assert math_service.pow_op(-2, 2) == 4

def test_factorial_op():
    assert math_service.factorial_op(0) == 1
    assert math_service.factorial_op(5) == 120
    with pytest.raises(ValueError):
        math_service.factorial_op(-1)

def test_fibonacci_op():
    assert math_service.fibonacci_op(0) == 0
    assert math_service.fibonacci_op(1) == 1
    assert math_service.fibonacci_op(6) == 8
    with pytest.raises(ValueError):
        math_service.fibonacci_op(-10)
