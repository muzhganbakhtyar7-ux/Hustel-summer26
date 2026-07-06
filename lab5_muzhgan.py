
# LAB 5 - WEEK 5 : The VibeCheck Bug Hunt

# Name: ___Muzhgan Bakhtyar___


# PART 1 - A function that greets a user


# BUG 1: Added a colon
def send_vibe():
    print("VibeCheck says: good energy only")


# BUG 2: Indented the print statement
def welcome_user():
    print("Welcome to VibeCheck!")


# PART 2 - A function that uses a variable


def show_mood():
    mood = "hyped"
    # BUG 3: Fixed variable name
    print(f"Today's mood is {mood}")


# PART 3 - A function with parameters

def make_shoutout(name, mood):
    return f"{name} is feeling {mood} today!"


# PART 4 - A function that counts hype points


def count_hype(likes, shares):
    # BUG 4: Add instead of subtract
    total = likes + shares
    return total


def final_message():
    print("Thanks for using VibeCheck!")


# RUNNING THE CODE

send_vibe()
welcome_user()
show_mood()

# BUG 6: Wrapped in print()
print(make_shoutout("Jordan", "creative"))

# BUG 7: Added the missing mood argument
print(make_shoutout("Alex", "chill"))

# BUG 8: Changed "ten" to the number 10
print(count_hype(10, 5))

# BUG 5: Moved the function call after the function definition
final_message()