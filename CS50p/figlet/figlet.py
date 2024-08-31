from pyfiglet import Figlet
from random import choice
import sys
figlet = Figlet()

if len(sys.argv) == 1 or (len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font")):
    try:
        if len(sys.argv) == 1:
            random_font = choice(figlet.getFonts())
            figlet.setFont(font=random_font)
            usr_inpt = input("Input: ")
            print(figlet.renderText(usr_inpt))
        else:
            figlet.setFont(font=sys.argv[2])
            usr_inpt = input("Input: ")
            print(figlet.renderText(usr_inpt))
    except:
        sys.exit("Invalid format")
else:
    sys.exit("Invalid format")
