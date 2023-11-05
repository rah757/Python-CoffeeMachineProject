import data

stillInGame = True

while stillInGame == True:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order in data.menu:
        print(f"You have ordered a {order}")
        print(f"The drink costs {data.menu[order]['cost']}$")
        print("Please enter your coins: ")
        # checkResources()
        # insertCoins()
        # makeCoffee()
        print(f"Here is your {order}, Enjoy!")

    elif order == "off":
        print("The machine is turning off... ")
        stillInGame = False
        break;
    elif order == "report":
        print("Printing machine report: \n")
#        showResources()             #shows all resources.
    else: 
        print("Enter a proper input.")


# def checkResources():

# def insertCoins():              #insert coins and calc total - check if tx was successful - if extra money, provide change

# def makeCoffee():              # reduce the coffee resources from total resources

# def showResources():