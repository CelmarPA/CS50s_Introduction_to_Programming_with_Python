def main():
    fraction = input("Fraction: ")

    print(gauge(convert(fraction)))


def convert(fraction):

    x, y = fraction.split("/")

    x, y = int(x), int(y)

    if x < 0 or y < 0:
        raise ValueError()

    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError()

    if y == 0:
        raise ZeroDivisionError()

    return str(round(x / y * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()
