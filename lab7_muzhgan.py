# ============================================================
# LAB 7 - MY OWN ORDERING APP
# Week 7 - Hack the Hood
# ============================================================
# Name: Muzhgan Bakhtyar
#
# My store sells: Sneakers and Slides
# ============================================================


# ============================================================
# DAY 1 - BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint

class Sneaker:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 3: The price guard
    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be below zero.")
        else:
            self.price = new_price

    # TICKET 5: Each item's own action
    def deliver(self):
        print("Shipping your sneakers!")


# TICKET 4: A second kind of item

class Slide(Sneaker):
    def deliver(self):
        print("Sliding out the door!")


# EXPLAIN:
# The same method name can do different things because
# each class has its own version of the method.


# TICKET 2: Make your real items

item1 = Sneaker("Air Max", 120)
item2 = Slide("Cloud Slide", 45)
item3 = Sneaker("Jordan 1", 150)

# PREDICT:
# print(item1.name) will show Air Max

print(item1.name)


# TICKET 3: Break it on purpose

# PREDICT:
# It will say the price cannot be below zero.

item1.set_price(-5)

# Message shown:
# Price cannot be below zero.


# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(item.name + " added!")

    # TICKET 9: Checkout
    def checkout(self):
        total = 0

        print("\nChecking out...")

        for item in self.items:
            item.deliver()
            total = total + item.price

        print("Total: $" + str(total))


# TICKET 7: My menu and my cart

store = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()


# TICKET 8: Let customers shop

# PREDICT:
# If I type 1, Air Max will be added to my cart.

while True:
    choice = input("Pick 1, 2, 3, or 'done': ")

    if choice == "done":
        break

    elif choice in store:
        cart.add(store[choice])

    else:
        print("Invalid choice.")


# TICKET 10: Test the whole app

# PREDICT:
# Choosing 1 then 2 then done will print:
#
# Air Max added!
# Cloud Slide added!
# Checking out...
# Shipping your sneakers!
# Sliding out the door!
# Total: $165

cart.checkout()