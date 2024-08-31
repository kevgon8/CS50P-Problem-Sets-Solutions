import inflect
p = inflect.engine()

Names = []

while True:
    try:
        name_input = input("Name: ")
        Names.append(name_input)
    except EOFError:
        break

print("Adieu, adieu, to", p.join(Names))
