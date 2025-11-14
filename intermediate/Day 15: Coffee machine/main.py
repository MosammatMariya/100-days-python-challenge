
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

def sufficient(ordered_ingredients):
    enough_i = True
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"Sorry, {item} is not available.")
            enough_i = False
    return enough_i

def process_coin():
    print("insert your coins:")
    total = int(input("how many pennies? ")) * 0.01
    total += int(input("how many nickels? ")) * 0.05
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many quaters? ")) * 0.25
    return total

def transaction(recived, cost_drink):
      if recived < cost_drink:
         print("sorry, you don't have enough coins.Money refunded")
         return False
      elif recived > cost_drink:
         r = round(recived - cost_drink,2)
         print(f"Thank you for your transaction.Here is your change {r}")
         global profit
         profit += cost_drink
         return True
      else:
        print("Thank you for your transaction.")

def make_coffee(drink_name, ingredients):
    """deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}")

going_on = True

while going_on:
    coffee = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if coffee == "end":
        going_on = False
        print("Thank you ")
    elif coffee =="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee]
        if sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction(payment, drink['cost']):
                make_coffee(coffee, drink["ingredients"])

