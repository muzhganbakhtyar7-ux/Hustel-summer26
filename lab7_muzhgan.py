# ============================================================
# LAB 7 - MY OWN ORDERING APP + EXTENSION
# Week 7 - Hack the Hood
# ============================================================
# Name: Muzhgan Bakhtyar
#
# My store sells: Sneakers and Slides
# ============================================================

# TICKET 1: import random
import random


# ============================================================
# DAY 1 - BUILD YOUR ITEMS
# ============================================================

class Sneaker:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 2: set_price guard
    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be below zero.")
        else:
            self.price = new_price

    # TICKET 5: item action
    def deliver(self):
        print("Shipping your sneakers!")


class Slide(Sneaker):
    def deliver(self):
        print("Sliding out the door!")


# EXPLAIN:
# The same method name can do different things because
# each class has its own version of the method.


# Make the real items
item1 = Sneaker("Air Max", 120)
item2 = Slide("Cloud Slide", 45)
item3 = Sneaker("Jordan 1", 150)

# PREDICT:
# print(item1.name) will show Air Max
print(item1.name)

# Break it on purpose
# PREDICT: It will say the price cannot be below zero.
item1.set_price(-5)

# Message shown:
# Price cannot be below zero.


# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(item.name + " added!")

    def checkout(self):
        total = 0

        print("\nChecking out...")

        for item in self.items:
            item.deliver()
            total = total + item.price

        print("Total: $" + str(total))


# Store menu
store = {
    "1": item1,
    "2": item2,
    "3": item3
}

# Empty cart
cart = Cart()


# ============================================================
# EXTENSION TICKET 1 - Random welcome
# ============================================================

welcome_messages = [
    "Hey there, happy shopping!",
    "Welcome to Prime Kicks!",
    "Thanks for visiting our sneaker store!"
]

print(random.choice(welcome_messages))


# ============================================================
# EXTENSION TICKET 2 - Put an item on sale
# ============================================================

item1.set_price(100)
print(item1.name + " is on sale for $" + str(item1.price) + "!")


# ============================================================
# EXTENSION TICKET 3 - Show the menu
# ============================================================

print("\nHere is what we have:")

for number, item in store.items():
    print(number + ": " + item.name + " - $" + str(item.price))


# ============================================================
# EXTENSION TICKET 4 - Handle wrong choices
# ============================================================

while True:
    choice = input("\nPick a number, or 'done': ")

    if choice == "done":
        break

    elif choice in store:
        cart.add(store[choice])

    else:
        print("Sorry, that's not on the menu!")


# ============================================================
# EXTENSION TICKET 5 - Print a receipt
# ============================================================

print("\n----- Your receipt -----")

for item in cart.items:
    print(item.name + " ..... $" + str(item.price))


# ============================================================
# EXTENSION TICKET 6 - Count the order
# ============================================================

print("You bought " + str(len(cart.items)) + " items.")


# Checkout
cart.checkout()