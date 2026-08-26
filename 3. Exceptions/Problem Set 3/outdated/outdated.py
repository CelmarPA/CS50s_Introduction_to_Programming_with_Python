months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:

    try:

        date = input("Date: ").strip()

        if date[0].isdigit():
            month, day, year = map(int, date.split("/"))

            if not months[month - 1]:
                raise ValueError()

            if day <= 0 or day >= 31:
                raise ValueError()

            if month <= 0 or month > 12:
                raise ValueError()

            break

        if date[0].isalpha():

            if "," not in date:
                raise ValueError()

            month, day, year = date.split(" ")
            day = int(day.replace(",", ""))

            if month not in months:
                raise ValueError()

            if day <= 0 or day > 31:
                raise  ValueError()

            month = months.index(month) + 1

            break

    except (ValueError, IndexError):
        pass


print(f"{year}-{month:02d}-{day:02d}")
