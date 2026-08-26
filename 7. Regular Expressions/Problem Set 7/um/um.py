import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"

    matches = re.findall(pattern, s, re.IGNORECASE)

    total = len(matches)

    return total


if __name__ == "__main__":
    main()
