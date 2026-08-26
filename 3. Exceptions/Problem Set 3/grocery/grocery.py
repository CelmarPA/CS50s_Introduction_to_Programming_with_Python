grocery_dict = {}


while True:
    try:
        item = input().lower()

        if item not in grocery_dict:
            grocery_dict[item] = 1

        else:
            grocery_dict[item] += 1

    except KeyError:
        pass

    except EOFError:
        print()

        break

sorted_dict = dict(sorted(grocery_dict.items()))

for key, value in sorted_dict.items():
    print(f"{value} {key.upper()}")
