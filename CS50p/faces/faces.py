def main():
    string = input()
    print(convert(string))

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

main()
