from random import randint
while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            break
    except ValueError:
        pass

random_int = randint(1, lvl)

while True:
    try:
        gssd = int(input("Guess: "))
        if gssd > 0:
            if gssd < random_int: 
                print("Too small!")
            elif gssd > random_int:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass