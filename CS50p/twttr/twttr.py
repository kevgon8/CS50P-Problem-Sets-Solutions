def main():
        str = input("Input: ")
        print("Output:", shorten(str))

def shorten(str):
        for i in str:
                if i in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
                        str = str.replace(i, "")
        return str

if __name__ == "__main__":
        main()
