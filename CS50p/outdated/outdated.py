months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    usr_date = input("Date: ")
    try:
        if usr_date[0].isalpha() == True:
            month_date, year = usr_date.split(", ")
            month, date = month_date.split(" ")
            date = int(date)
            month = months.index(month)+1
            if ( 1 <= month <= 12 and 1 <= date <= 31):
                break
        elif usr_date[0].isnumeric() == True:
            month, date, year = usr_date.split("/")
            month = int(month)
            date = int(date)
            if ( 1 <= month <= 12 and 1 <= date <= 31):
                break
    except:
        pass

print(f"{year}-{"{:02d}".format(month)}-{"{:02d}".format(date)}")
