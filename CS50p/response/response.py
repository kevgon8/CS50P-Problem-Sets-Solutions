from validator_collection import checkers

usr_input = input("What's your email address? ")
if checkers.is_email(usr_input) == True:
    print("Valid")
else:
    print("Invalid")
