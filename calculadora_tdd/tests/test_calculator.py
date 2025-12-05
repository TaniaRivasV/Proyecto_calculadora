from calculadora_tdd.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_resta():
    calc = Calculator()
    assert calc.resta(10, 4) == 6
    assert calc.resta(3, -2) == 5
