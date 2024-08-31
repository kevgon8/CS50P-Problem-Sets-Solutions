import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False and sys.argv[2].endswith(".csv") == False:
    sys.exit("Is not a csv file")
else:
    list = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                surname, name = row["name"].split(", ")
                list.append({"first": name, "last": surname,"house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["col1", "col2", "col3"])
        writer.writerow({"col1": "first", "col2": "last", "col3": "house"})
        for i in list:
            writer.writerow({"col1": i["first"], "col2": i["last"], "col3": i["house"]})
