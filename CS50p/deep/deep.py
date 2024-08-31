def main():
    que = input("What is the Answer to the Great Question of Life, the Universe and Everything?: ").strip().lower()
    if func(que):
        print("Yes")
    else:
        print("No")

def func(x):
    match x:
        case "42" | "forty two" | "forty-two" :
            return True
        case _:
            return False

main()
