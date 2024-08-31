import json
import requests
import sys

if len(sys.argv) ==  1:
    sys.exit("Missing command-line argument")

try:
    input = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
k = response.json()
dollars = float(k["bpi"]["USD"]["rate_float"])
print(f"${input*dollars:,.4f}")
