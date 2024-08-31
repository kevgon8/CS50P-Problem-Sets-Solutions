import inflect
from datetime import date
import sys

def main():
    usr_input = input("Date of birth: ")
    try:
        year, month, date = usr_input.split("-")
    except ValueError:
        sys.exit("Invalid format :(")
    print(mins_convert(year, month, date))

def mins_convert(yr, mnth, dy):
    w = inflect.engine()
    try:
        dte = date(int(yr), int(mnth), int(dy))
    except ValueError:
        return "Invalid date :("

    todays_date = date.today()
    days1 = todays_date-dte
    final_days = int(str(days1).replace(" days, 0:00:00", ""))
    total_mins = final_days*24*60
    nmbr_wrd = w.number_to_words(total_mins, andword="").capitalize() + " minutes"
    return nmbr_wrd

if  __name__ == "__main__":
    main()
