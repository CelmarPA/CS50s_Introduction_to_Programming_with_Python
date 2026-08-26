import sys
import csv
from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file = sys.argv[1]

if not file.endswith(".csv"):
    sys.exit("Not a CSV file")

pizzas = []

try:
    with open(file, "r") as f:
        reader = csv.DictReader(f)

        for line in reader:
            pizzas.append(line)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizzas, headers="keys", tablefmt="grid"))
