import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    qtd = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")


API_KEY = "49ed7efb400910e1241ec1e0247acb46010c276736f5818d07198e2f610c8769"

url = "https://rest.coincap.io/v3/assets/bitcoin"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:

    response = requests.get(url, headers=headers)

    btc_price = float(response.json()["data"].get("priceUsd"))

except requests.RequestException:
    sys.exit()

price = qtd * btc_price

print(f"${price:,.4f}")
