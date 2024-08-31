def main():
    greet = input("Greeting: ").strip().lower()
    print(value(greet))

def value(greet):

    def detect_first_letter(x):
        if x.startswith("h"):
            return True
        else:
            return False

    def hello_or_not(y):
        if y.startswith("hello"):
            return True
        else:
            return False

    if detect_first_letter(greet):
        if hello_or_not(greet):
            return 0
        else:
            return 20
    else:
        return 100

if __name__ =="__main__":
    main()
