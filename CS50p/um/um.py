import re

def main():
    print(count(input("Input: ")))

def count(usr):
    if matches := re.findall(r"\bum\b", usr.lower()):
        return len(matches)

if __name__ == "__main__":
    main()
