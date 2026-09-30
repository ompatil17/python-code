menu = {
    "espreso":
        {"ingredint":
             {"water": 50,
              "coffee": 18},
         "cost": 1.5}
    ,
    "latta":
        {"ingredint":
             {"water": 200,
              "coffee": 24,
              "milk": 150},
         "cost": 2.5}
    ,
    "cappuccino":
        {"ingredint":
             {"water": 250, "coffee": 24, "milk": 100},
         "cost": 3.0}
}
profit = 0
resources = {"water": 300,
             "milk": 200,
             "coffee": 100}

def is_resourse_suff(order_ingredints):

    for items in order_ingredints:
        if order_ingredints[items] >= resources[items]:
            print(f"sorry less ingredint{items}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry money refunded.")
        return False

def make_coffee(drink_name, order_ingredint):
    for item in order_ingredint:
        resources[item] -= order_ingredint[item]
    print(f"Here is your drink {drink_name}")

def process_coins():
    """return the total money """
    print("please insert the coin")
    total = int(input("How many Quarters?: "))*0.25
    total += int(input("How many Dimes?: "))*0.10
    total += int(input("How many Nickles?: "))*0.05
    total += int(input("How many Pennies?: "))*0.01
    return total

is_on = True
while is_on :
    choice= input("What would you like to order(espreso/latta/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']} ")
        print(f"milk:{resources['milk']} ")
        print(f"coffee:{resources['coffee']} ")
        print(f"Money:${profit}")

    else:
        drink= menu[choice]
        if is_resourse_suff(drink["ingredint"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
            make_coffee(choice, drink["ingredint"])
























