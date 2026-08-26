def main():
    word = input("Input: ")

    print(shorten(word))


def shorten(word):

    list_letters = []

    for letter in word:

        if letter not in ["a", "e", "i", "o", "u"]:
            list_letters.append(letter)

    return "".join(list_letters)


if __name__ == "__main__":
    main()
