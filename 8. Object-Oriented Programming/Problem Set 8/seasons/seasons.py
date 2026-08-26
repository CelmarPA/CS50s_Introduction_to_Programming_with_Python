import sys
import re
import inflect
from datetime import date, datetime


def main():
    birthdate = input("Date of Birth: ")
    season = Seasons(birthdate)

    print(season)


class Seasons:

    def __init__(self, birthdate):
        self.birthdate = Seasons.validate_date(birthdate)
        self.minutes = self.calculate_minutes()
        self.p = inflect.engine()

    @classmethod
    def validate_date(cls, birthdate):
        pattern = r"\d{4}-\d{2}-\d{2}"

        if re.fullmatch(pattern, birthdate):
            try:
                return datetime.strptime(birthdate, "%Y-%m-%d")

            except ValueError:
                sys.exit("Invalid date")

        else:
            sys.exit("Invalid date")

    def calculate_minutes(self):
        now = datetime.combine(date.today(), datetime.min.time())
        minutes = (now - self.birthdate).total_seconds() / 60

        return round(minutes)

    def numbers_to_words(self):
        return self.p.number_to_words(self.minutes).replace(" and ", " ").capitalize() + " minutes"

    def __str__(self):
        return f"{self.numbers_to_words}"


if __name__ == "__main__":
    main()
