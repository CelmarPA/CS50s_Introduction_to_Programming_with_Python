import random


cards = ["jack", "queen", "king"]


def main():
    # print(random.choice(cards))
    # print(random.choices(cards, k=2))
    # print(random.sample(cards, k=2))
    # print(random.choices(cards, weights=[75, 20, 5], k=2))

    random.seed(1)
    print(random.choices(cards, k=2))

main()