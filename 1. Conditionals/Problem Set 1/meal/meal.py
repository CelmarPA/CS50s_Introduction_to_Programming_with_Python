def main():
    time = input("What time is it? ").strip()

    time_cv = convert(time)

    if 7 <= time_cv <= 8:
        print("breakfast time")

    elif 12 <= time_cv <= 13:
        print("lunch time")

    elif 18 <= time_cv <= 19:
        print("dinner time")


def convert(time):

    parts = time.split(" ")

    if len(parts) == 2:
        hours_min, am_pm = parts

    else:
        hours_min = parts[0]
        am_pm = "a.m."

    hours, minutes = hours_min.split(":")

    if am_pm == "p.m." and int(hours) != 12:
        hours = int(hours) + 12

    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()