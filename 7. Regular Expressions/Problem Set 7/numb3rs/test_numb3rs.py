import pytest
from numb3rs import validate


def test_valid():
    ips = ["127.0.0.1", "0.0.0.0", "255.255.255.255", "192.168.1.1"]

    for ip in ips:
        assert validate(ip)


def test_invalid():
    ips = ["256.0.0.1", "0.256.0.1", "0.0.256.1", "0.0.0.256"]

    for ip in ips:
        assert not validate(ip)


def test_left_zero():
    ips = ["01.2.3.4", "1.02.3.4", "1.2.03.4", "1.2.3.04"]

    for ip in ips:
        assert not validate(ip)


def test_invalid_formats():
    ips = ["127.0.0", "127.0.0.1.1", "127..0.1", ".127.0.0.1", "127.0.0.1."]

    for ip in ips:
        assert not validate(ip)


def test_error():
    with pytest.raises(TypeError):
        validate()
