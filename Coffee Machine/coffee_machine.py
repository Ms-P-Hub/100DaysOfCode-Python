MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 12,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 13,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def machine_on():
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
        )
    elif choice == "latte":
        check_resources(choice)
        machine_on()
    elif choice == "espresso":
        check_resources(choice)
        machine_on()
    elif choice == "cappuccino":
        check_resources(choice)
        machine_on()
    else:
        return print("Powering Off...")


def payment(choice):
    due = print(f"Your {choice} is R{MENU[choice]['cost']}")
    print("Please insert coins.")
    one = float(input("How many R1: "))
    two = float(input("How many R2: "))
    five = float(input("How many R5: "))

    amount = one + (two * 2) + (five * 5)

    if amount >= due:
        print(f"Here is R{amount - due} in change.")
        global money
        money += due
    else:
        print(f"Money is sort with R{due - amount}")
        payment(choice)


def check_resources(choice):

    if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Running low on Coffee. Sorry.")
    elif resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Running low on Water. Sorry.")
    elif not choice == "espresso" and resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            print("Running low on Milk. Sorry.")
    else:
        payment(choice)
        resources["coffee"] = (
            resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
        )
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        if not choice == "espresso":
            resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
        print(f"Here is your {choice}☕ Enjoy!")


machine_on()
