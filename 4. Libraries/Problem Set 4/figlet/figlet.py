import sys
import random
from pyfiglet import Figlet, FigletFont, FontNotFound

fonts = FigletFont.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
    f = Figlet(font=font)

elif len(sys.argv) == 3:

    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    try:
        font = sys.argv[2]

        f = Figlet(font=f"{font}")

    except FontNotFound:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")


text = input("Input: ")

print("Output:")
print(f.renderText(f"{text}"))
