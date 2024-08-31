import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'"(https?)://(?:www\.)?(youtube\.com)/embed(/.+?")', s)
    if matches:
        a = matches.group(1)
        if a.endswith("p"):
            a = a.replace("p", "ps")

        b = matches.group(2).replace("be.com", ".be")
        c = matches.group(3).replace('"', '')
        final_link = f"{a}://{b}{c}"
        return final_link
    else:
        return None

if __name__ == "__main__":
    main()
