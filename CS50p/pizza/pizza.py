from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Is not a csv file")
else:
    list = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for line in reader:
                list.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")

print(tabulate(list, headers="firstrow", tablefmt="grid"))
