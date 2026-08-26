import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]
extensions = (".jpeg", ".jpg", ".png")

if not input_file.endswith(extensions) or not output_file.endswith(extensions):
    sys.exit("Invalid input")

if input_file.split(".")[-1] != output_file.split(".")[-1]:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(input_file, "r") as image, Image.open("shirt.png") as shirt:
        size = shirt.size
        image = ImageOps.fit(image=image, size=size)
        image.paste(shirt, (0, 0), mask=shirt)
        image.save(output_file)

except FileNotFoundError:
    sys.exit("Input does not exist")
