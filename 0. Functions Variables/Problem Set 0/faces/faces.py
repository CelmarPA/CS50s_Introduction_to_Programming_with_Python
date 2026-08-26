def main():
    text = input().strip()

    print(convert(text))


def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == '__main__':
    main()