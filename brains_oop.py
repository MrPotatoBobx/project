class DataManagment():

    def opt_a(self):
        data = open("items.txt", "r")
        list = data.read()
        print (list)
        data.close()
    # adding new items
    def opt_b(self, item, amount):
        data = open("items.txt", "a")
        writeitem = "\n" + item + " - " + str(amount)
        data.write(writeitem)
    def opt_c(self, value):
        data = open("items.txt", "r")
        list = data.readlines()
        data.close()
        #print (list)
        print ("You have selected ", value, " Please choose what to do with it (type ? for help)")
        prompt = "(" + str(value) + ")" + ">"
        opts = input(prompt)
        if  opts == "?":
            print("a <number> - add a number to your option\ns <number> - take away numbers from your selection\nn <name> - edit item name\ne - exit")
        elif opts[0].lower() == "a":
            self.add(value, opts[2])


    def add(self, value, number):
        data = open("items.txt", "r")
         filedata = data.read()
         



def inputb():
    a = DataManagment("null", 0)
    try:
        iteminput = input("Please enter the name of the item:")
        amountinput = int(input("Please enter the amount of the item:"))
        a.opt_b(iteminput, amountinput)
    except ValueError:
        print ("Please enter a valid amount")
        print ("--------------------------")
        inputb()

a = DataManagment()
a.opt_c(1)
