import pytest
from datetime import datetime
from seasons import Seasons

def test_valid():
    seasons = Seasons("1999-01-01")
    assert seasons.numbers_to_words == "Fourteen million, five hundred forty-one thousand, one hundred twenty minutes"


def test_leap_year():
    with pytest.raises(SystemExit):
        seasons = Seasons("1999-02-31")
        seasons.numbers_to_words()


def test_minutes():
    seasons = Seasons("1999-01-01")
    assert seasons.calculate_minutes() == 1_4541_120


def test_validate():
    assert Seasons.validate_date("1999-01-01")  == datetime(1999, 1, 1, 0, 0)


def test_error():
    with pytest.raises(TypeError):
        seasons = Seasons()
        seasons.numbers_to_words()
