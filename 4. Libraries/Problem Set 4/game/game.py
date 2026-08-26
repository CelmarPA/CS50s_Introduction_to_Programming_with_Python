from random import randint


def main():

    level = get_positive_int("Level")
    number = randint(1, level)

    while True:
        guess = get_positive_int("Guess")

        if guess < number:
            print("Too small!")

        elif guess > number:
            print("Too large!")

        else:
            print("Just right!")
            break


def get_positive_int(prompt):

    while True:

        try:
            value = int(input(f"{prompt}: "))

            if value > 0:
                break

        except ValueError:
            pass

    return value


if __name__ == "__main__":
    main()
