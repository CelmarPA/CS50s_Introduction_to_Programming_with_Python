import pytest
from project import (
    get_cheapest_flight,
    generate_report,
    save_report,
    get_city_code,
    get_access_token,
    search_flights,
    search_flight_offers,
    menu
)


flights = [
    {
        "total_amount": "500.00",
        "owner": {"name": "Airline A"},
        "slices": [
            {
                "segments": [
                    {
                        "origin": {"city_name": "London"},
                        "destination": {"city_name": "New York"},
                        "departing_at": "2026-10-10T10:00:00",
                        "arriving_at": "2026-10-10T13:00:00"
                    }
                ]
            },
            {
                "segments": [
                    {
                        "origin": {"city_name": "New York"},
                        "destination": {"city_name": "London"},
                        "departing_at": "2026-10-20T15:00:00",
                        "arriving_at": "2026-10-20T18:00:00"
                    }
                ]
            }
        ]
    },
    {
        "total_amount": "400.00",
        "owner": {"name": "Airline B"},
        "slices": [
            {
                "segments": [
                    {
                        "origin": {"city_name": "London"},
                        "destination": {"city_name": "New York"},
                        "departing_at": "2026-10-10T12:00:00",
                        "arriving_at": "2026-10-10T15:00:00"
                    }
                ]
            },
            {
                "segments": [
                    {
                        "origin": {"city_name": "New York"},
                        "destination": {"city_name": "London"},
                        "departing_at": "2026-10-20T17:00:00",
                        "arriving_at": "2026-10-20T20:00:00"
                    }
                ]
            }
        ]
    }
]

cheapest_flights = [
    {
        "price": "400.00",
        "airline": "Airline B",
        "outbound": {
            "origin": "London",
            "destination": "New York",
            "departure": "2026-10-10T12:00:00",
            "arrival": "2026-10-10T15:00:00"
        },
        "return": {
            "origin": "New York",
            "destination": "London",
            "departure": "2026-10-20T17:00:00",
            "arrival": "2026-10-20T20:00:00"
        }
    }
]


def test_get_cheapest_flight():
    result = get_cheapest_flight(flights, return_data=True)

    assert result["price"] == "400.00"
    assert result["airline"] == "Airline B"


def test_generate_report():
    report = generate_report(cheapest_flights)

    assert "FLIGHT PRICES REPORT" in report
    assert "London → New York" in report
    assert "Airline: Airline B" in report
    assert "Price: $400.00" in report
    assert "Outbound:" in report
    assert "Return:" in report


def test_save_report(tmp_path):
    report = "FLIGHT PRICES REPORT\nPrice: $400.00"

    file = tmp_path / "report.txt"

    save_report(report, file)

    assert file.read_text() == report

def test_get_city_code():
    result = get_city_code("London")

    assert "LON" in result


def test_get_access_token():
    result = get_access_token()

    assert isinstance(result, str)
    assert result != ""


def test_search_flights():
    result = search_flights(
        ["LON"],
        ["NYC"],
        "2026-10-10",
        "2026-10-20",
        30,
        "economy"
    )

    assert len(result) == 1


def test_search_flight_offers():
    result = search_flight_offers(
        "LON",
        "NYC",
        "2026-10-10",
        "2026-10-20",
        30,
        "economy"
    )

    assert result is not None
    assert isinstance(result, list)


def test_menu(monkeypatch):
    inputs = iter([
        "London",
        "New York",
        "2026-10-10",
        "2026-10-20",
        "30",
        "1"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = menu()

    assert result["origin"] == "London"
    assert result["destination"] == "New York"
    assert result["passenger_age"] == 30
    assert result["cabin_class"] == "economy"
