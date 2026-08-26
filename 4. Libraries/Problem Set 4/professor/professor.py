import random


def main():
    level = get_level()
    count = 0
    correct = 0

    while count < 10:
        x = (generate_integer(level))
        y = generate_integer(level)
        incorrect = 0

        while incorrect < 3:
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == (x + y):
                    correct += 1
                    break

                else:
                    print("EEE")
                    incorrect += 1

            except ValueError:
                print("EEE")
                incorrect += 1

        if incorrect == 3:
            print(f"{x} + {y} = {x + y}")

        count += 1

    print(f"Score: {correct}")


def get_level():

    while True:

        try:
            level = int(input(f"Level: "))

            if 1 <=  level <= 3:
                break

        except ValueError:
            pass

    return level


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(100, 999)

    else:
        raise ValueError


if __name__ == "__main__":
    main()
