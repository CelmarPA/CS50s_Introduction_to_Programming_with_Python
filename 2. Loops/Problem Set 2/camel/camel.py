camel_case = input("camelCase: ")

list_words = []

for letter in camel_case:

    if letter.isupper():
        list_words.append("_")
        list_words.append(letter)

    else:
        list_words.append(letter)

snake_case = "".join(list_words).lower()

print(f"snake_case: {snake_case}")
