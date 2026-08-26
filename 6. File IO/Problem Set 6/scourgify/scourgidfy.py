import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(input_file, "r") as file, open(output_file, "w", newline="") as new_file:
        field_names = ["first", "last", "house"]
        reader = csv.DictReader(file)
        writer = csv.DictWriter(new_file, fieldnames=field_names)
        writer.writeheader()

        for line in reader:
            last, first = line["name"].split(",")
            house = line["house"]

            writer.writerow({"first": first.strip(), "last": last.strip(), "house": house})

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")