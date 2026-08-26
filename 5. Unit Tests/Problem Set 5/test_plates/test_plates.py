import pytest
from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True


def test_invalid():
    assert is_valid("CS05") == False


def test_alpha_valid():
    assert is_valid("AB") == True


def test_alpha_invalid():
    assert is_valid("A2") == False


def test_minimum():
    assert is_valid("CS") == True


def test_maximum():
    assert is_valid("AAA222") == True


def test_any_length():
    assert is_valid("AAA2222222") == False


def test_punctuation():
    assert is_valid("CS50-") == False


def test_beginning_numbers():
    assert is_valid("50CS50") == False


def test_number_places():
    assert is_valid("AAA22A") == False


def test_error():
    with pytest.raises(TypeError):
        is_valid()
