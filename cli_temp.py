#import functions from other files
from brains import opt_a, opt_b
#print the welcome screen
print ("Welcome to Golden City product management, Please select an option. \nA:view stock\nB:New item\nC:select item")
#ask and read option
def find_option():
    option = input("> ")
    if option.lower() == "a":
        opt_a()
    elif option.lower() == "b":
        opt_b()
    elif option.lower() == "c":
        print("you selected c")
    else:
        print("please select a valid option.")
    find_option()
find_option()
