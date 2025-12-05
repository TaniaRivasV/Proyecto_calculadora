from calculadora_tdd.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_resta():
    calc = Calculator()
    assert calc.resta(10, 4) == 6
    assert calc.resta(3, -2) == 5

def test_division():
    calc = Calculator()
    assert calc.div(10, 2) == 5
    assert calc.div(5, 2) == 2.5

def test_division_by_zero():
    calc = Calculator()
    import pytest
    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)

def test_multiplication():
    calc = Calculator()
    assert calc.mul(3, 4) == 12
    assert calc.mul(2.5, 2) == 5
    assert calc.mul(-3, 3) == -9
    assert calc.mul(0, 100) == 0

import pytest

def test_sqrt_positive():
    calc = Calculator()
    assert calc.sqrt(4) == pytest.approx(2.0, rel=1e-3)
    assert calc.sqrt(9) == pytest.approx(3.0, rel=1e-3)
    assert calc.sqrt(2) == pytest.approx(1.414, rel=1e-3)

def test_sqrt_zero():
    calc = Calculator()
    assert calc.sqrt(0) == 0

def test_sqrt_negative():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.sqrt(-5)
def test_exp_basic():
    calc = Calculator()
    assert calc.exp(0) == pytest.approx(1.0, rel=1e-3)
    assert calc.exp(1) == pytest.approx(2.718, rel=1e-3)
    assert calc.exp(2) == pytest.approx(7.389, rel=1e-3)

def test_exp_negative():
    calc = Calculator()
    assert calc.exp(-1) == pytest.approx(0.367879, rel=1e-3)

