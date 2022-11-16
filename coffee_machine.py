import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

#TODO:3 Report Function (report)
#TODO:4 Check resources sufficient
#TODO:5 Check transaction succesful 
#TODO:6 Make coffe

def espresso():
    """Make espresso"""
    if resources["water"] < MENU["espresso"]["ingredients"]["water"] or  resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        print ("Sorry there is not enough water.")
    else:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        resources["money"] += 1.5
        print ("Here is your espresso.☕ Enjoy")
    
    
def latte():
    """Make latte"""
    if resources["water"] < MENU["latte"]["ingredients"]["water"] or  resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] or \
        resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print ("Sorry there is not enough water, coffee or milk.")
    else:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources ["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["money"] += 2.5
        print ("Here is your latte.☕ Enjoy")
       

def cappuccino():
    """Make cappuccino"""
    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"] \
        or resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        print ("Sorry there is not enough water, coffee or milk.")
    else:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources ["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["money"] += 3.0
        print ("Here is your cappuccino.☕ Enjoy")
        
#TODO:4 Payment function

def espresso_payment():
    print ("Please insert coins")
    quarters = int(input ("How many quarters: "))
    dimes = int(input ("How many dimes?: "))
    nickles = int(input ("How many nickles?: "))
    pennies = int(input ("How many pennies?: "))
    coins = quarters* 0.25 + dimes * 0.10 + nickles *0.05 + pennies * 0.01

    espresso_cost = coins - MENU["espresso"]["cost"] 
    if MENU["espresso"]["cost"] > coins:
        print ("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${round(espresso_cost,2)} in change")
        

def latte_payment():
    print ("Please insert coins")
    quarters = int(input ("How many quarters: "))
    dimes = int(input ("How many dimes?: "))
    nickles = int(input ("How many nickles?: "))
    pennies = int(input ("How many pennies?: "))
    coins = quarters* 0.25 + dimes * 0.10 + nickles *0.05 + pennies * 0.01
    latte_cost = coins - MENU["latte"]["cost"]
    if MENU["latte"]["cost"] > coins:
        print ("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${round(latte_cost,2)} in change")


def cappuccino_payment():
    print ("Please insert coins")
    quarters = int(input ("How many quarters: "))
    dimes = int(input ("How many dimes?: "))
    nickles = int(input ("How many nickles?: "))
    pennies = int(input ("How many pennies?: "))
    coins = quarters* 0.25 + dimes * 0.10 + nickles *0.05 + pennies * 0.01
    cappuccino_cost = coins - MENU["cappuccino"]["cost"] 
    if MENU["cappuccino"]["cost"] > coins:
        print ("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${round(cappuccino_cost,2)} in change")
    
#TODO:1. Prompt user by asking "What would you like?"
#TODO:2  Turn off the cofee Machine by entering "off" to the prompt
while True:
    choice = input("  What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso":
        espresso_payment()
        espresso()
    if choice == "latte":
        latte_payment()
        latte()
    if choice == "cappuccino":
        cappuccino_payment()
        cappuccino()
    if choice == "report": 
        print (f"Water:{resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    if choice == "off":
        sys.exit()
        












