amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount_due = amount_due - coin

change_owed = str(amount_due).replace("-", "")
print("Change Owed:", change_owed)
