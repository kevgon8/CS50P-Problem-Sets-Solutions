def main():
    usr = input("camelCase: ")
    itr(usr)


def itr(x):
    for i in x:
        if i.isupper():
            x = x.replace(i, "_" + i)
        elif i.islower():
            x = x.replace(i, i)
    print("snake_case:", x.lower())

main()
