import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'^<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9_\-]+)".*?></iframe>$'

    match = re.search(pattern, s)

    if match:
        result = re.sub(r"https?://(?:www\.)?", "https://", match.group(1))

        return re.sub("youtube.com/embed", "youtu.be", result)

    else:
        return None


if __name__ == "__main__":
    main()
