expression = input("Expression: ").strip().split(" ")

x = float(expression[0])
y = expression[1]
z = float(expression[2])

if y == "+":
    print(round(x + z, 1))

elif y == "-":
    print(round(x - z, 1))

elif y == "*":
    print(round(x * z, 1))

elif y == "/":
    print(round(x / z, 1))
