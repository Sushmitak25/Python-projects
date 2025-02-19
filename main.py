import art

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#item_cost = {MENU['cost']}

def print_report():
    print(f"water: {resources['water']} ml")
    print(f"milk: {resources['milk']} ml")
    print(f"coffee: {resources['coffee']} ml")
    print(f"Money : {profit}")




#check if the ingredients needed for the ordered items are sufficient.
def check_available(order_ingredients):
    for item in  order_ingredients :
        if order_ingredients[item] > resources[item]:
            print(f"sorry we do not have sufficient {item}")
            return False
    return True



def coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: $(0.25)"))
    dimes = int(input("how many dimes?: $(0.10)"))
    nickles = int(input("how many nickles?: $(0.05)"))
    pennies = int(input("how many pennies?: $(0.01)"))
    user_total = (quarters*0.25) + (nickles*0.05) + (dimes*0.10) + (pennies*0.10)
    return round(user_total , 2)

def transaction(received_money, item_cost):
    if received_money > item_cost:
        change = round(received_money - item_cost, 2)
        print(f"Here is your change {change} $")
        global profit
        profit+= item_cost
        return True
    else:
        print(f"sorry that's not enough money for you to buy a drink 🥺")
        return False

def make_coffee(d_name , order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {d_name} ☕️. Enjoy!")



machine_on = True

while machine_on:
    print(art.logo)
    u_choice = input("what would you love to have? (espresso/latte/cappuccino): ").lower()
    if u_choice == "off":
        print("turning off the machine. Goodbye!")
        machine_on = False
    elif u_choice == "report":
        print_report()

    else:
        drink = MENU[u_choice]
        if check_available(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                make_coffee(u_choice, drink["ingredients"])
    # elif u_choice in MENU:
    #     drink = MENU[u_choice]
    #     if check_available(drink["ingredients"]):
    #         payment = coins()
    #         if transaction(payment, drink["cost"]):
    #             make_coffee(choice, drink["ingredients"])
    #     print("❓ Invalid option. Please choose again.")



























