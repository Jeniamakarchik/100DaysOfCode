if __name__ == "__main__":
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
        "money": 0
    }

    while True:
        cmd = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if cmd == "off":
            break
        elif cmd == "report":
            print(f'''
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${resources["money"]}
            ''')
        elif cmd in ["espresso", "latte", "cappuccino"]:
            if cmd != "espresso" and MENU[cmd]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk.")
                continue
            if MENU[cmd]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water.")
                continue
            if MENU[cmd]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough milk.")
                continue

            print("Please insert coins.")
            money = 0
            money += int(input("How many quarters? ")) * 0.25
            money += int(input("How many dimes? ")) * 0.1
            money += int(input("How many nickles? ")) * 0.05
            money += int(input("How many pennies? ")) * 0.01

            if money < MENU[cmd]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif money > MENU[cmd]["cost"]:
                print(
                    f"Here is ${money - MENU[cmd]['cost']} dollars in change.")

            resources["water"] -= MENU[cmd]["ingredients"]["water"]
            resources["coffee"] -= MENU[cmd]["ingredients"]["coffee"]
            if cmd != "espresso":
                resources["milk"] -= MENU[cmd]["ingredients"]["milk"]
            resources["money"] += MENU[cmd]["cost"]

            print(f"Here is your {cmd} ☕. Enjoy!")
