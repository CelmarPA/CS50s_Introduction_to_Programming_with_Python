WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    # print("Your letters are: A I P C R H G")
    #
    # while len(WORDS) > 0:
    #
    #     print(f"{len(WORDS)} words left!")
    #
    #     guess = input("Guess a word: ").upper()
    #
    #     # TODO: Check if guess is in dictionary]
    #     if guess == "GRAPHIC":
    #         WORDS.clear()
    #         print("You've won!")
    #
    #     if guess in WORDS.keys():
    #         points = WORDS.pop(guess)
    #
    #         print(f"Good job! Your scored {points} points.")
    #
    #
    # print("That's the game!")

    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


main()
