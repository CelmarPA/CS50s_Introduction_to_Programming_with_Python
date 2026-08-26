def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):
    part_number = ""

    if not s[:2].isalpha():
        return False

    for char in s:
        if char.isdigit():
            index = s.index(char)
            part_number = s[index:]

            break

    if part_number:

        if part_number[0] == "0":
            return False

        if not part_number.isdigit():
            return False

    return True


if __name__ == "__main__":
    main()
