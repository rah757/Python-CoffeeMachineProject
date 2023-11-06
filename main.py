import data

def startGame(stillInGame):
    while stillInGame == True:
        order = input("\nWhat would you like? (espresso/latte/cappuccino):").lower()
        if order in data.menu:
            print(f"\nYou have ordered a {order}")
            print(f"\nThe drink costs {data.menu[order]['cost']}$")
            print("\nPlease insert your coins: ")
            checkResources(order)        # testing
            insertCoins(order)
            makeCoffee(order)
            print(f"\nHere is your {order}, Enjoy!")

        elif order == "off":
            print("\nThe machine is turning off...  ")
            stillInGame = False
            break;
        
        elif order == "report":
            print("\nPrinting machine report:\n \n")
            showResources()             #shows all resources.

        else: 
            print("\nEnter a proper input.")

        if input("\nwould you like to order another coffee? (y/n): ") == 'n':
            stillInGame = False
            print("\nHope you enjoyed your order, please visit again soon! \n")
        else:
            stillInGame = True


def ingredientFinder(order,item):
    return data.menu[order]['ingredients'][item], data.resources[item]

def checkResources(order):
    water, resourceWater = ingredientFinder(order, 'water')
    milk, resourceMilk = ingredientFinder(order, 'milk')
    coffee, resourceCoffee = ingredientFinder(order, 'coffee')
    requirements = [water, milk, coffee]
    resources = [resourceWater, resourceMilk, resourceCoffee]
    enough = True

    for i in range(0,len(resources)):
        if requirements[i] <= resources[i]:
            enough = True
        else:
            enough = False
            break;
    
    if enough == False:
        print("Not enough resources in coffee machine, please visit some other time.")
        stillInGame = False
        return


def insertCoins(order):              #insert coins and calc total - check if tx was successful - if extra money, provide change
    values = {
        'quarter':0.25,
        'dime':0.1,
        'nickel':0.05,
        'penny':0.01,
    }
    total = 0
    for element in values:
        total += int(input(f"Enter the number of {element}: ")) * values[element]
    if total >= data.menu[order]['cost']:
        print(f"\nYour change is {total - data.menu[order]['cost']}$")
        makeCoffee(order)
    else:
        print("not enough money")
        return

def makeCoffee(order):              # reduce the coffee resources from total resources
    for element in data.resources:
        data.resources[element] -= data.menu[order]['cost']

def showResources():
    print("----- Resources left in stock -----")
    for element in data.resources:
        print(f"{element} = {data.resources[element]}   ",end='')
    print("\n")


stillInGame = True                       # make it true to start game 
startGame(stillInGame)                   # Start game at the end of the program so that all the functions get defined first.