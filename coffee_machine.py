def run_coffee_maker():
    what_do_you_want = input("What would you like to do? Type 'get coffee' or 'check stock': ")
    if what_do_you_want == "get coffee":
        payment_register = {}
        chosen_flavor = input("Which flavor would you like? Type 'espresso', 'latte', or 'cappuccino': ")
        if are_resources_sufficient(coffee_flavors, chosen_flavor, coffee_making_resources) == "Enough Resources":
            make_coffee(coffee_flavors[chosen_flavor], coffee_making_resources)
            collect_payment(payment_register)
            amount_paid = calculate_amount_paid(payment_register, accepted_coins_in_cents)
            change = calculate_change(amount_paid, coffee_flavors[chosen_flavor]["price"])
            if "Your change is" in change:
                print(enjoy_coffee_message(chosen_flavor))
                print_receipt(coffee_flavors, chosen_flavor, change)
            else:
                print(change)
        else:
            print(are_resources_sufficient(coffee_flavors, chosen_flavor, coffee_making_resources))
    elif what_do_you_want == "check stock":
        print_report()


coffee_flavors = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 1.50
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.50
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.00
    }
}

coffee_making_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

accepted_coins_in_cents = {
    "penny": 1,
    "nickel": 5,
    "dime": 10,
    "quarter": 25
}


def are_resources_sufficient(menu, ordered_coffee, remaining_resources):
    ordered_flavor = menu[ordered_coffee]
    if remaining_resources["water"] - ordered_flavor["water"] < 0:
        return "Not enough water"
    elif remaining_resources["coffee"] - ordered_flavor["coffee"] < 0:
        return "Not enough coffee"
    elif remaining_resources["milk"] - ordered_flavor["milk"] < 0:
        return "Not enough milk"
    else:
        return "Enough Resources"


def make_coffee(ordered_coffee, resources):
    resources["water"] = resources["water"] - ordered_coffee["water"]
    resources["milk"] = resources["milk"] - ordered_coffee["milk"]
    resources["coffee"] = resources["coffee"] - ordered_coffee["coffee"]


def collect_payment(payment_register):
    payment_register["penny"] = int(input("How many pennies will you pay? "))
    payment_register["nickel"] = int(input("How many nickels will you pay? "))
    payment_register["dime"] = int(input("How many dimes will you pay? "))
    payment_register["quarter"] = int(input("How many quarters will you pay? "))


def calculate_amount_paid(coins, conversion_scheme):
    pennies_to_coins = coins["penny"] * conversion_scheme["penny"]
    nickels_to_coins = coins["nickel"] * conversion_scheme["nickel"]
    dimes_to_coins = coins["dime"] * conversion_scheme["dime"]
    quarters_to_coins = coins["quarter"] * conversion_scheme["quarter"]
    total_cents_paid = pennies_to_coins + nickels_to_coins + dimes_to_coins + quarters_to_coins
    dollar_amount_paid = total_cents_paid / 100
    return dollar_amount_paid


def calculate_change(amount_paid, order_total):
    if amount_paid < order_total:
        return "Sorry, that's not enough money. Money refunded"
    elif amount_paid == order_total:
        return "No change"
    else:
        return f"Your change is ${amount_paid - order_total}"


def enjoy_coffee_message(ordered_coffee):
    return f"Here is your {ordered_coffee}. Enjoy!"


def print_receipt(menu, coffee_flavor, change):
    chosen_flavor = menu[coffee_flavor]
    print(f"Flavor: {coffee_flavor}")
    print(f"Water: {chosen_flavor['water']}")
    print(f"Coffee: {chosen_flavor['coffee']}")
    print(f"Milk: {chosen_flavor['milk']}")
    print(f"Change: {change}")


def print_report():
    print(coffee_making_resources)


run_coffee_maker()