from menu import MENU
from menu import resources


bank = []

penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25


def order(user_order, MENU):
    """Returns product ingredients from dictionary MENU if available."""
    if user_order in MENU:
        return MENU[user_order]['ingredients']


def price():
    """Returns the price of items pers order"""
    price = MENU[user_order]['cost']
    return price


def calculate_bank(bank, price):
    """Calculates generated money"""
    bank.append(price())
    return sum(bank)


def report_resources(resources, bank):
    """Prints available resources"""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f" The available money is ${sum(bank)}")


def prepare_order(resources):
    """Subtracts the required resources from the dictionary of resources"""
    resources['water'] = resources['water'] - MENU[user_order]['ingredients']['water']
    if 'milk' not in MENU[user_order]['ingredients']:
        MENU[user_order]['ingredients']['milk'] = 0
        resources['milk'] = resources['milk'] - MENU[user_order]['ingredients']['milk']
    else:
        resources['milk'] = resources['milk'] - MENU[user_order]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[user_order]['ingredients']['coffee']
    return resources


def check_if_enough(resources):
    if resources['water'] < 0 or resources['milk'] < 0 or resources['coffee'] < 0:
        return False

def count_coins():
    """Counts the amount of money inserted"""
    sum = penny * number_of_pennies + nickel * number_of_nickels + dime * number_of_dimes + quarter * number_of_quarters
    return sum


def check_sum(count_coins):
    """Checks if the inserted sum is equal to the cost"""
    if count_coins() > price():
        change = round(count_coins() - price(),2)
        print(f"Your change is {change}")
    elif count_coins() == price():
        print("Thank you.")
    else:
        sum = count_coins()
        print(f"Sorry. You inserted ${sum}. It is not enough.")


end_game = False
while end_game is False:

    user_order = input("What would you like? (espresso/latte/cappuccino?)")

    if user_order == "report":
        report_resources(resources, bank)
        break
    elif user_order == "off":
        end_game = True
        break
    else:
        order(user_order, MENU)

    prepare_order(resources)

    if check_if_enough(resources) is False:
        print("Not enough resources.")
        break
    else:
        check_if_enough(resources)

    number_of_pennies = 0  # int(input("Pennies: " ))
    number_of_nickels = 0  # int(input("Nickels: "))
    number_of_dimes = 0  # int(input("Dimes: "))
    number_of_quarters = int(input("Quarters: "))

    price()
    count_coins()
    check_sum(count_coins)
    calculate_bank(bank,price)

print("Come again.")