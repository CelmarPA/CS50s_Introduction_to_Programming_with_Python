import pytest
from um import count


def test_zero():
    assert count("yummy") == 0


def test_one():
    assert count("hello, um, world") == 1


def test_two():
    assert count("um, hello, um, world") == 2


def test_case_insensitive():
    assert count("Um, thanks, um...") == 2


def test_error():
    with pytest.raises(TypeError):
        count()
