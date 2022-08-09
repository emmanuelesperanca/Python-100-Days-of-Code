from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

end_loop = False
menu = Menu()
options = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not end_loop:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    order = CoffeeMaker()
    if choice == "off":
        end_loop = True
    elif choice == "report":
        order.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
