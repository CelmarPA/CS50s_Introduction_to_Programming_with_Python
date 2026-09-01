import os
import requests
import itertools
from pathlib import Path
from dotenv import load_dotenv


def main() -> None:
    """Run the flight price monitoring application."""

    config_environment()
    flight_data = menu()

    origin: str = flight_data["origin"]
    destination: str = flight_data["destination"]
    departure_date: str = flight_data["departure_date"]
    return_date: str = flight_data["return_date"]
    passenger_age: int = flight_data["passenger_age"]
    cabin_class: str = flight_data["cabin_class"]

    print("\nSearching for city codes...")
    origins = get_city_code(origin)
    destinations = get_city_code(destination)

    if origins is None or destinations is None:
        return

    print("\nStarting flight search...")

    flights = search_flights(
        origins,
        destinations,
        departure_date,
        return_date,
        passenger_age,
        cabin_class
    )

    cheapest_flights = []

    for flight in flights:
        cheapest = get_cheapest_flight(
            flight["offers"],
            return_data=True
        )

        cheapest_flights.append(cheapest)

    print("\nGenerating report...")
    report = generate_report(cheapest_flights)

    save_report(report)
    print("\nReport saved to report.txt!")


def config_environment() -> None:
    """Load environment variables from the .env file."""

    base_dir = Path(__file__).resolve().parent

    # Load the .env file located in the same directory as this script.
    load_dotenv(dotenv_path=base_dir / ".env")


def get_access_token() -> str:
    """Return the Duffel API access token."""

    return os.getenv('DUFFEL_ACCESS_TOKEN', "")


def search_flight_offers(
    origin: str,
    destination: str,
    departure_date: str,
    return_date: str,
    age: int,
    cabin_class: str
) -> list[dict] | None:
    """Search for flight offers between two airports."""

    url = "https://api.duffel.com/air/offer_requests"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Duffel-Version": "v2",
        "Authorization": f"Bearer {get_access_token()}"
    }

    payload = {
        "data": {
            "cabin_class": cabin_class,
            "slices": [
                {
                    "origin": origin,
                    "destination": destination,
                    "departure_date": departure_date
                }
            ],
            "passengers": [
                {
                    "age": age
                }
            ]
        }
    }

    if return_date:
        payload["data"]["slices"].append(
            {
                "origin": destination,
                "destination": origin,
                "departure_date": return_date
            }
        )

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            return response.json()["data"]["offers"]

        else:
            print(f"\nAPI error ({response.status_code}): {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"\nConnection error: {e}")

        return None


def search_flights(
    origins: list[str],
    destinations: list[str],
    departure_date: str,
    return_date: str,
    age: int,
    cabin_class: str
) -> list[dict]:

    """Search for flight offers for every origin and destination combination."""
    combinations = itertools.product(origins, destinations)

    flights = []

    for origin, destination in combinations:
        offers = search_flight_offers(
            origin,
            destination,
            departure_date,
            return_date,
            age,
            cabin_class
        )

        flights.append({
            "origin": origin,
            "destination": destination,
            "offers": offers
        })

    return flights


def get_cheapest_flight(
    flights: list[dict],
    return_data: bool = False
) -> dict:
    """Return the cheapest flight from a list of flight offers."""

    cheapest = min(flights, key=lambda x: float(x["total_amount"]))

    cheapest_flight = {
        "price": cheapest["total_amount"],
        "airline": cheapest["owner"]["name"],
        "outbound": {
            "origin": cheapest["slices"][0]["segments"][0]["origin"]["city_name"],
            "destination": cheapest["slices"][0]["segments"][0]["destination"]["city_name"],
            "departure": cheapest["slices"][0]["segments"][0]["departing_at"],
            "arrival": cheapest["slices"][0]["segments"][0]["arriving_at"]
        }
    }

    if return_data:
        cheapest_flight["return"] = {
            "origin": cheapest["slices"][1]["segments"][0]["origin"]["city_name"],
            "destination": cheapest["slices"][1]["segments"][0]["destination"]["city_name"],
            "departure": cheapest["slices"][1]["segments"][0]["departing_at"],
            "arrival": cheapest["slices"][1]["segments"][0]["arriving_at"]
        }

    return cheapest_flight


def get_city_code(city: str) -> list[str] | None:
    """Return the IATA city codes matching the given city name."""

    url = f"https://api.duffel.com/places/suggestions?query={city.lower()}"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Duffel-Version": "v2",
        "Authorization": f"Bearer {get_access_token()}"
    }

    try:
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        data = response.json()["data"]

        iata_city_codes = {item["iata_city_code"] for item in data if item["type"] == "city"}

        return list(iata_city_codes)

    except requests.exceptions.RequestException as e:
        print(f"\nConnection error: {e}")

        return None


def generate_report(flights: list[dict]) -> str:
    """Generate a text report containing the prices and details of the flights."""

    report = "FLIGHT PRICES REPORT\n"
    report += "====================\n\n"

    for flight in flights:
        report += f'{flight["outbound"]["origin"]} → '
        report += f'{flight["outbound"]["destination"]}\n'

        report += f'Airline: {flight["airline"]}\n'
        report += f'Price: ${flight["price"]}\n\n'

        report += "Outbound:\n"
        report += f'{flight["outbound"]["departure"]} → '
        report += f'{flight["outbound"]["arrival"]}\n\n'

        report += "Return:\n"
        report += f'{flight["return"]["departure"]} → '
        report += f'{flight["return"]["arrival"]}\n\n'

        report += "--------------------\n\n"

    return report


def save_report(report: str, filename: str = "report.txt") -> None:
    """Save the flight price report to a text file."""

    with open(filename, "w") as file:
        file.write(report)


def menu() -> dict:
    """Display the menu and collect the flight search parameters from the user."""

    print("=== Flight Prices Monitor ===")

    origin = input("Origin city: ")
    destination = input("Destination city: ")

    departure_date = input("Departure date (YYYY-MM-DD): ")
    return_date = input("Return date (YYYY-MM-DD): ")

    passenger_age = int(input("Passenger age: "))

    print("\nCabin class:")
    print("1 - Economy")
    print("2 - Premium Economy")
    print("3 - Business")
    print("4 - First")

    cabin_options = {
        "1": "economy",
        "2": "premium_economy",
        "3": "business",
        "4": "first"
    }

    cabin_class = cabin_options[input("Choose cabin class: ")]

    return {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "return_date": return_date,
        "passenger_age": passenger_age,
        "cabin_class": cabin_class
    }


if __name__ == "__main__":
    main()
