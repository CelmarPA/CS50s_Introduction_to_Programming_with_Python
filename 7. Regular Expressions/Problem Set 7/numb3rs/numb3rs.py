import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}"

    return bool(re.fullmatch(pattern, ip))


if __name__ == "__main__":
    main()
