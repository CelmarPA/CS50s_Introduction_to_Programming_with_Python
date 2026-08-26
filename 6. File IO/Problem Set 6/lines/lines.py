import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file = sys.argv[1]

if not file.endswith(".py"):
    sys.exit("Not a Python file")

count = 0

try:
    with open(file, "r") as f:
        for line in f:
            clean_line = line.strip()

            if not clean_line or clean_line.startswith("#"):
                continue

            else:
                count += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
