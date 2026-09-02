# Flight Prices Monitor

#### Video Demo: <https://youtu.be/vf6wPH8Qw9w>

#### Description:

Flight Prices Monitor is a Python application that searches for flight offers using the Duffel API and 
identifies the cheapest available flight for each possible origin and destination combination.

The application asks the user for an origin city, destination city, departure date, optional return date, passenger age,
and cabin class. The user can choose between Economy, Premium Economy, Business, and First class.

The return date is optional. If the user provides a return date, the application searches for a round trip. If the user
leaves the return date empty, the application searches for a one-way flight.

Instead of requiring the user to know airport or IATA codes, the application accepts city names. It uses Duffel's Places
Suggestions API to search for matching cities and obtain their IATA city codes. Since a city name can sometimes 
correspond to more than one city code, the application keeps all matching city codes.

The application then creates every possible combination between the origin and destination city codes. For example, if 
the origin produces two possible city codes and the destination also produces two city codes, the program searches 
four different route combinations.

For each combination, the application sends a request to Duffel's Flights API and searches for available flight offers.
For round trips, the request contains two flight slices: one for the outbound journey and one for the return journey.
For one-way flights, only the outbound slice is included.

After receiving the flight offers, the application finds the cheapest offer by comparing the `total_amount` value
returned by the API. From the cheapest offer, the program extracts the price, airline, origin, destination, departure
time, and arrival time. For round trips, the application also extracts the corresponding return flight information.

The results are then passed to the report generation function. The application creates a text report containing
the routes, airline, price, outbound flight information, and when it exists, the return flight information. The final
report is saved as `report.txt`.

## Installation

Clone or download the project and navigate to its directory:

```bash
cd Final Project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

On Linux or macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

After installing the dependencies and configuring the API token, run the application with:

```bash
python project.py
```

The program displays a menu and asks for the flight search information.

For example:

```text
=== Flight Prices Monitor ===

Origin city: London
Destination city: New York

Departure date (YYYY-MM-DD): 2026-10-10
Return date (YYYY-MM-DD): 2026-10-20

Passenger age: 30

Cabin class:
1 - Economy
2 - Premium Economy
3 - Business
4 - First

Choose cabin class: 1
```

The return date is optional. To search for a one-way flight, simply leave the return date empty:

```text
Return date (YYYY-MM-DD):
```

The application then searches the possible city-code combinations and retrieves the available flight offers.

After the search is completed, the application generates a report and saves it as:

```text
report.txt
```

A round-trip report contains outbound and return information:

```text
FLIGHT PRICES REPORT
====================

London → New York
Airline: Airline
Price: $400.00

Outbound:
2026-10-10T12:00:00 → 2026-10-10T15:00:00

Return:
2026-10-20T17:00:00 → 2026-10-20T20:00:00
```

For a one-way flight, the report contains only the outbound information.

## Running the Tests

The project uses `pytest` for automated testing.

To run the test suite, execute:

```bash
pytest test_project.py
```

The tests cover the main functionality of the application, including finding the cheapest flight, generating and saving 
reports, retrieving city codes, retrieving the API token, searching for flights and flight offers, and processing 
user input.

## Files

### `project.py`

This is the main application file. It contains the functions responsible for the application's functionality.

`main()` controls the execution flow of the application.

`menu()` collects the user's flight search parameters, including the cities, dates, passenger age, and cabin class.

`config_environment()` loads environment variables from the `.env` file.

`get_access_token()` retrieves the Duffel API access token.

`get_city_code()` searches Duffel's Places Suggestions API and returns the matching IATA city codes.

`search_flight_offers()` sends a flight search request to Duffel's Flights API. It adds a return slice only when a 
return date is provided.

`search_flights()` creates the possible origin and destination combinations and searches for offers for each combination.

`get_cheapest_flight()` finds the cheapest offer and extracts the relevant flight information. 
It handles both one-way and round-trip flights.

`generate_report()` creates the text report and includes return information only when the flight is a round trip.

`save_report()` saves the generated report to `report.txt`.

### `test_project.py`

This file contains the automated tests for the project using `pytest`.

The tests verify the main functionality of the application, including finding the cheapest flight, generating a report, 
saving the report to a file, retrieving city codes, retrieving the API token, searching for flights, searching for 
flight offers, and processing user input.

### `requirements.txt`

This file contains the Python dependencies required by the project.

The project uses packages such as `requests`, `python-dotenv`, and `pytest`.

### `report.txt`

This file is generated by the application after a flight search. It contains the cheapest flight information found for 
each searched route.

## Design Choices

One of the main design choices was to allow users to enter city names instead of requiring IATA codes. This makes the 
application easier to use because users generally know the names of their cities but may not know their airport or city 
codes.

Another important decision was to search every possible combination of the returned origin and destination city codes. 
This allows the application to compare different possible routes instead of assuming that a city name always corresponds 
to only one code.

For example, if Duffel returns two possible origin city codes and two possible destination city codes, the application 
searches all four combinations:

```text
Origin 1 → Destination 1
Origin 1 → Destination 2
Origin 2 → Destination 1
Origin 2 → Destination 2
```

The application also supports both one-way and round-trip searches. Rather than requiring separate search functions, the
same flight-search logic is used for both cases. The return slice is added only when the user provides a return date.

I also separated the application's functionality into individual functions. Each function has a specific responsibility,
such as obtaining city codes, searching for offers, finding the cheapest flight, generating the report, or saving the 
report.

The project uses a `.env` file to store the Duffel API token instead of hardcoding credentials directly in the source 
code. The `config_environment()` function loads the environment variables using `python-dotenv`, and `get_access_token()`
retrieves the token when it is needed.

For the CS50P submission, the project includes a fallback test token in `get_access_token()` so that the application 
can still run without requiring the evaluator to configure a `.env` file. In a production environment, 
sensitive API credentials should be stored in environment variables and should never be committed to the source code.

## What I Learned

This project allowed me to apply several concepts from CS50P in a practical application. I worked with functions, lists,
dictionaries, exception handling, file handling, environment variables, type hints, docstrings, external APIs, JSON 
responses, and automated testing with pytest.

Working with the Duffel API also gave me experience dealing with structured API responses and extracting the specific 
information needed by an application.

One of the more interesting parts of the project was handling city searches that can return multiple IATA city codes. 
Instead of selecting only the first result, the application searches all possible combinations and compares the 
resulting flight offers.

The project also evolved to support both one-way and round-trip searches. This required handling the optional return 
date throughout the flight search, cheapest-flight processing, and report generation.

The project started as an idea for monitoring flight prices and evolved into a complete command-line application that 
accepts user input, communicates with an external API, processes flight offers, identifies the cheapest options, 
and generates a report.

# API and Test Data

This project uses the Duffel API to search for flight offers. During development and demonstration, the project uses 
Duffel's test environment. The flight offers and prices returned by the test environment are simulated and should not 
be considered real-world flight prices or available bookings.

The purpose of this project is to demonstrate the integration with a flight search API, handling multiple airport 
combinations, finding the cheapest available offer for each combination, and generating a price report.