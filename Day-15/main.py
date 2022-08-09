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
}

close_program = False
value = 0
money = 0


def check_resources(choice):
    for item in MENU[choice]['ingredients']:
        if resources[item] < MENU[choice]['ingredients'][item]:
            print('Sorry there is not enough', item)
            return False


def report():
    global money
    print('Water =', resources['water'], 'ml.')
    print('Milk =', resources['milk'], 'ml.')
    print('Coffee =', resources['coffee'], 'g.')
    print(f'Money = ${money}.')


def payment(choice):
    global money
    print('Please, insert the coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    value = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    print(value)
    if value >= MENU[choice]['cost']:
        change = round(value - MENU[choice]['cost'], 2)
        print(f'Here is {change} in change')
        money += MENU[choice]['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffee_type(choice):
    for item in MENU[choice]['ingredients']:
        resources[item] -= MENU[choice]['ingredients'][item]
    print('Here is your', choice, '☕️. Enjoy!')


while not close_program:
    if not close_program:
        choice = input('What would you like? (espresso/latte/cappuccino): ')
        if choice == 'report':
            report()
        elif choice == 'off':
            close_program = True
        else:
            if not check_resources(choice):
                if not payment(choice):
                    coffee_type(choice)
