import pytest
from main.assignment_3 import f, euler_method, runge_kutta

def test_euler_method():
    result = euler_method(f, 0, 1, 2, 10)
    # Check Euler result to 10 decimal places
    assert pytest.approx(result, rel=1e-10) == 1.2446380979332121

def test_runge_kutta():
    result = runge_kutta(f, 0, 1, 2, 10)
    # Check Runge-Kutta result to 10 decimal places
    assert pytest.approx(result, rel=1e-10) == 1.251316587879806
