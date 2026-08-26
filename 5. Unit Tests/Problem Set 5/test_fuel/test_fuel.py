import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_negative():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_empty():
    assert gauge(1) == "E"


def test_full():
    assert gauge(100) == "F"


def test_99_full():
    assert gauge(99) == "F"


def test_percentage():
    assert gauge(50) == "50%"
