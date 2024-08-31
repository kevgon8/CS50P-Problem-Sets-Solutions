sum = input("Expression: ")
x, y, z = sum.split(" ")
n1 = float(x)
n2 = float(z)

if y == "+":
    print(f"{n1 + n2: .1f}")
elif y == "-":
    print(f"{n1 - n2: .1f}")
elif y == "*":
    print(f"{n1 * n2: .1f}")
elif y == "/" and z == "0":
    print("Number can't be divided by zero")
elif y == "/":
    print(f"{n1 / n2: .1f}")
