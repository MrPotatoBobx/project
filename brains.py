import time


def opt_a():
    data = open("items.txt", "r")
    list = data.read()
    print (list)


def opt_b():
    try:
        data = open("items.txt", "a")
        itemname = input("Please enter item name:")
        amount = int(input("Enter the amount:"))
        writeitem = "\n" + itemname + " - " + str(amount)
        data.write(writeitem)
    except ValueError:
        print("Enter a valid number")
        print("--------------------")
        opt_b()
def opt_c():
    print("do optc soon")
