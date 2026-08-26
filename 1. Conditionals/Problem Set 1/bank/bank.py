greeting = input("Greeting: ").strip().lower().split(",")[0]

if greeting == "hello":
    print("$0")

elif greeting[0] == "h":
    print("$20")

else:
    print("$100")
