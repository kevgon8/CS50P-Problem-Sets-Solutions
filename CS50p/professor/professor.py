import random

def main():
    score = 0
    i = 0
    lvl = get_level()
    while i < 10:
        n1, n2 = generate_integer(lvl)
        for j in range(3):
            usr_ans = int(input(f"{n1} + {n2} = "))
            if j == 2 and usr_ans != n1 + n2:
                i = i + 1
                print("EEE")
                print(f"{n1} + {n2} = {n1 + n2}")
                break
            elif usr_ans != n1 + n2:
                print("EEE")
                pass
            elif usr_ans == n1 + n2:
                score = score + 1
                i = i + 1
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            usr_lvl = int(input("Level: "))
            if 1 <= usr_lvl <= 3:
                return usr_lvl
        except ValueError:
            pass

def generate_integer(lvl):
    if lvl == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif lvl == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif lvl == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y

if __name__ == "__main__":
    main()
