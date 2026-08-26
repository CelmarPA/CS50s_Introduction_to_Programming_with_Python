import pytest
from bank import value


def test_zero():
    assert value("hello") == 0


def test_twenty():
    assert value("hola") == 20


def test_hundred():
    assert value("ei") == 100


def test_upper():
    assert value("HOLA") == 20


def test_error():
    with pytest.raises(TypeError):
        value()
