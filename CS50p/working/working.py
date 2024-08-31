import re

def main():
    print(convert(input("Hours: ")))

def convert(usr):
    matches = re.search(r"^((?:1?\d)(?::\d\d)?) (AM|PM) to ((?:1?\d)(?::\d\d)?) (AM|PM)$", usr)

    # Naming variables and making arrangements if the usr didn't put minutes and invalid format
    try:
        if ":" in matches.group(1):
            h1, m1 = matches.group(1).split(":")
        else:
            h1 = matches.group(1)
            m1 = 0
        ampm1 = matches.group(2)
        if ":" in matches.group(3):
            h2, m2 = matches.group(3).split(":")
        else:
            h2 = matches.group(3)
            m2 = 0
        ampm2 = matches.group(4)
    except AttributeError:
        raise ValueError("Invalid time format")

    # Validating time
    if int(h1) > 12 or int(h2) > 12 or int(m1) > 59 or int(m2) > 59:
        raise ValueError("Invalid time")

    # Main conversion
    if ampm1 == "AM":
        if h1 == "12":
            h1 = "0"
        time1 = f"{h1:0>2}:{m1:0>2}"
    elif ampm1 == "PM":
        if h1 == "12":
            h1 = "12"
        else:
            h1 = int(h1)+12
        time1 = f"{h1:0>2}:{m1:0>2}"

    if ampm2 == "AM":
        if h2 == "12":
            h2 = "0"
        time2 = f"{h2:0>2}:{m2:0>2}"
    elif ampm2 == "PM":
        if h2 == "12":
            h2 = "12"
        else:
            h2 = int(h2)+12
        time2 = f"{h2:0>2}:{m2:0>2}"

    return (f"{time1} to {time2}")

if __name__ == "__main__":
    main()
