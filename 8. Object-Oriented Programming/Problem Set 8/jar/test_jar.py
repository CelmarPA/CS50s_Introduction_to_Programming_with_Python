import pytest
from jar import Jar


def test_init():
    jar = Jar()

    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(2)

    assert str(jar) == "🍪🍪"


def test_initial_size():
    jar = Jar()

    assert jar.size == 0


def test_deposit():
    jar = Jar()
    jar.deposit(5)

    assert jar.size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)

    assert jar.size == 3


def test_deposit_value_error():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.deposit(-5)


def test_withdraw_value_error():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(-5)
