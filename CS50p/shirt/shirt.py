import sys
from os.path import splitext
from PIL import ImageOps, Image

def main():
    check_commandline()
    try:
        usr_img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt_img = Image.open("shirt.png")

    size = shirt_img.size
    resized_usr_img = ImageOps.fit(usr_img, size)
    resized_usr_img.paste(shirt_img, shirt_img)

    resized_usr_img.save(sys.argv[2])

def check_commandline():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    extension1 = splitext(sys.argv[1])
    extension2 = splitext(sys.argv[2])

    if check_extension(extension1[1]):
        sys.exit("Invalid Input extension")
    if check_extension(extension2[1]):
        sys.exit("Invalid Output extension")

    if extension1[1].lower() != extension2[1].lower():
        sys.exit("Input and Output have different extention")

def check_extension(usr_file):
    if usr_file not in [".jpg", ".jpeg", ".png"]:
        return True
    else:
        return False

main()
