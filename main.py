import data

StillInGame = True


while StillInGame == True:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order in data.menu:
        print(f"you have ordered a {data.menu[order]}")
    elif order == "off":
        print("The machine is turning off... ")
        StillInGame = False
        break;
    elif order == "report":
        print("Printing machine report: \n")
#        showResources()             #shows all resources.
    else: 
        print("Enter a proper input.")
