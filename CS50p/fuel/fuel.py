def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
    try:
        num, denom = fraction.split("/")
        new_num = int(num)
        new_denom = int(denom)
        x = float(new_num/new_denom)
        if x <= 1:
            return int(x*100)
        elif x > 1:
           raise ValueError("Numerator has to be greater than the Denominator")
    except ValueError:
        raise ValueError("Invalid format")
    except ZeroDivisionError:
        raise ZeroDivisionError("Number can't be divided by zero")

def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{percent:.0f}%"

if __name__ == "__main__":
    main()
