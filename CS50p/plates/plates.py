def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    for i in range(2):
        if s[i].isalpha() == False:
            return False

    if len(s) == 4:
        sub_str = s[2:4]
        x, y = [*sub_str]
        if x.isnumeric() == True and y.isalpha() == True:
            return False
    elif len(s) == 5:
        sub_str = s[2:5]
        x, y, z = [*sub_str]
        if x.isnumeric() == True and y.isalpha() == True and z.isalpha() == True:
            return False
        elif x.isalpha() == True and y.isnumeric() == True and z.isalpha() == True:
            return False
        elif x.isnumeric() == True and y.isnumeric == True and z.isalpha() == True:
            return False
        elif x.isnumeric() == True and y.isalpha() == True and z.isnumeric() == True:
            return False
    elif len(s) == 6:
        sub_str = s[2:6]
        x, y, z, k = [*sub_str]
        if x.isnumeric() == True and y.isalpha() == True and z.isalpha() == True and k.isnumeric() == True:
            return False
        elif x.isnumeric() == True and y.isalpha() == True and z.isalpha() == True and k.isalpha() == True:
            return False
        elif x.isalpha() == True and y.isnumeric() == True and z.isalpha() == True and k.isalpha() == True:
            return False
        elif x.isalpha() == True and y.isalpha() == True and z.isnumeric() == True and k.isalpha() == True:
            return False
        elif x.isnumeric() == True and y.isnumeric() == True and z.isalpha() == True and k.isalpha() == True:
            return False
        elif x.isalpha() == True and y.isnumeric() == True and z.isnumeric() == True and k.isalpha() == True:
            return False
        elif x.isnumeric() == True and y.isalpha() == True and z.isnumeric() == True and k.isalpha() == True:
            return False
        elif x.isnumeric() == True and y.isnumeric() == True and z.isnumeric() == True and k.isalpha() == True:
            return False
        elif x.isalpha() == True and y.isnumeric() == True and z.isalpha() == True and k.isnumeric() == True:
            return False
        elif x.isnumeric() == True and y.isalpha() == True and z.isnumeric() == True and k.isnumeric() == True:
            return False
        elif x.isnumeric() == True and y.isnumeric() == True and z.isalpha() == True and k.isnumeric() == True:
            return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    k = 0
    while k < len(s):
        if s[k] in [".", " ", "!", "?"]:
            return False
        k += 1

    return True

main()
