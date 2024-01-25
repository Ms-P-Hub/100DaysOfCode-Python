from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from art import logo

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    print(logo)
    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
