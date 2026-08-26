import re


def main():
    print(convert(input("Hours: ")))


def hours(h):
    time, period = h.split(" ")

    if 1 <= len(time) <= 2:
        if period == "AM":
            if time == "12":
                return "00:00"

            time = f"{time.zfill(2)}:00"

        else:
            if time != "12":
                time = f"{str(int(time) + 12)}:00"

            else:
                time = "12:00"

        return time

    elif 4 <= len(time) <= 5:
        hour, minute = time.split(":")

        if period == "AM":
            if hour == "12":
                hour = "00"

            else:
                hour = hour.zfill(2)

            time = f"{hour}:{minute}"

        else:
            if hour != "12":
                hour = str(int(hour) + 12)

            time = f"{hour}:{minute}"

        return time

    return None

def convert(s):
    pattern = r"((?:[1-9]|1[0-2])(?::(?:0[0-9]|[1-5][0-9]))? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?::(?:0[0-9]|[1-5][0-9]))? (?:AM|PM))"

    match = re.fullmatch(pattern, s)

    if match:
        result = f"{hours(match.group(1))} to {hours(match.group(2))}"

        return result

    else:
        raise ValueError()


if __name__ == "__main__":
    main()

