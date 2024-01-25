from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from art import logo
coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
# menu_item = MenuItem()

print(logo)
choice = input(f"What would you like? {menu.get_items()}: ").lower()

if choice == "report":
    coffee.report()
    money.report()
# elif coffee.is_resource_sufficient(choice):
    
#     MoneyMachine.make_payment()
#     CoffeeMaker.make_coffee(choice)
    



