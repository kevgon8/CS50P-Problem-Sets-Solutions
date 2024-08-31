import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Is not a python file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    i = 0
    for one_line in lines:
        one_line = one_line.strip()
        if one_line.startswith("#") or len(one_line) == 0:
            pass
        else:
            i += 1

    print("Number of lines:", i)
