import pytest
from twttr import shorten


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_only_vowels():
    assert shorten("aeiou") == ""


def test_numbers():
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("Hello, world") == "Hll, wrld"


def test_empty():
    with pytest.raises(TypeError):
        shorten()
