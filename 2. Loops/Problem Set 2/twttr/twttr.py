vowels = ["a", "e", "i", "o", "u"]

text = input("Input: ")

list_letters = []

for letter in text:

    if letter.lower() not in vowels:
        list_letters.append(letter)

new_text = "".join(list_letters)

print(f"Output: {new_text}")
