import pytest
from working import convert


def test_valid_hours():
    valid_times = [
        ("1 AM to 2 PM", "01:00 to 14:00"),
        ("9 AM to 5 PM", "09:00 to 17:00"),
        ("12 AM to 12 PM", "00:00 to 12:00"),
        ("12 PM to 12 AM", "12:00 to 00:00"),
        ("1:00 AM to 2:00 PM", "01:00 to 14:00"),
        ("9:15 AM to 5:30 PM", "09:15 to 17:30"),
        ("10:05 AM to 11:45 PM", "10:05 to 23:45"),
        ("11:59 AM to 12:00 PM", "11:59 to 12:00"),
        ("12:00 AM to 12:59 PM", "00:00 to 12:59"),
        ("3:30 PM to 11:45 PM", "15:30 to 23:45"),
    ]

    for time, expected in valid_times:
        assert convert(time) == expected


def test_invalid_hours():
    invalid_times = [
        "0 AM to 5 PM",
        "13 AM to 5 PM",
        "9:60 AM to 5 PM",
        "9:5 AM to 5 PM",
        "9:00 AM to 5:60 PM",
        "9:00 AM to 13:00 PM",
        "9AM to 5PM",
        "9 AM 5 PM",
        "9:00 XM to 5:00 PM",
        "12:00 AM - 5:00 PM",
    ]

    for time in invalid_times:
        with pytest.raises(ValueError):
            convert(time)


def test_boundaries():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:59 AM to 12:59 PM") == "00:59 to 12:59"
    assert convert("11:59 AM to 11:59 PM") == "11:59 to 23:59"


def test_error():
    with pytest.raises(TypeError):
        convert()
