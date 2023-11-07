import data

print(data.logo)

def startGame(stillInGame):
    while stillInGame == True:
        order = input("\nWhat would you like? (espresso/latte/cappuccino):").lower()
        if order in data.menu:
            print(f"\nYou have ordered a {order}")
            print(f"\nThe drink costs {data.menu[order]['cost']}$\n")
            enoughResources = True
            enoughResources = checkResources(order) #checks if theres enough resources and returns true or false - also prints resources insufficient message if necessary
            if enoughResources:
                insertCoins(order)       # input coins and provide change accordingly - print insufficient if not enough coins
                print(f"\nHere is your {order}, Enjoy!")
            else:
                stillInGame = False

        elif order == "off":
            print("\nThe machine is turning off...  ")
            stillInGame = False
        
        elif order == "report":
            print("\nPrinting machine report:\n \n")
            showResources()                             #shows all resources.

        else: 
            print("\nEnter a proper input.")

        if stillInGame:
            if input("\nwould you like to order another coffee? (y/n): ") == 'n':
                stillInGame = False
                print("\nHope you enjoyed your order, please visit again soon! \n")
            else:
                stillInGame = True

def checkResources(order):
    enough = True

    for item in data.menu[order]['ingredients']:
        if data.menu[order]['ingredients'][item] <= data.resources[item]:
            enough = True
        else:
            enough = False
            break;

    if enough == False:
        print("Not enough resources in coffee machine, please visit some other time.")
        return False
    else:
        return True


def insertCoins(order):              #insert coins and calc total - check if tx was successful - if extra money, provide change
    values = {
        'quarters':0.25,
        'dimes':0.1,
        'nickels':0.05,
        'pennies':0.01,
    }
    total = 0
    for element in values:
        total += int(input(f"Insert {element}: ")) * values[element]
    if total >= data.menu[order]['cost']:
        print(f"\nYour change is {total - data.menu[order]['cost']}$")
        makeCoffee(order)
    else:
        print("not enough money")
        return

def makeCoffee(order):             # reduce the coffee resources from total resources
    for element in data.resources:
        data.resources[element] -= data.menu[order]['ingredients'][element]

def showResources():
    print("----- Resources left in stock -----")
    for element in data.resources:
        print(f"{element} = {data.resources[element]}   ",end='')
    print("\n")


stillInGame = True                       # make it true to start game 
startGame(stillInGame)                   # Start game at the end of the program so that all the functions get defined first.