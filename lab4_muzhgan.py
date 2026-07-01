# Muzhgan Bakhtyar | Lab 5 | Intro to Python
# Ticket 1
# PREDICT: Ages 17, 25, and 13 will get "Access granted" and Ages 11 and 9 will get "Too young"

ages = [17, 11, 25, 9, 13]
for age in ages:
    if age >=13:
        print(f"{age} - Access granted")
    else:
        print(f"{age} - Too young")
#EXPLAIN: The codes show which age is too young and which is old enough to get access.

# Ticket 2
# PREDICT: Maybe if I type "no" after the first check, the loop will stop.
keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Enter your age: "))
    if age >= 13:
        print("Access granted")
    else:
        print("Too young")
    keep_checking = input("check another age? (yes/no): ")
# EXPLAIN: When i typed "no" on the first check, the loop only runs one time.

# Ticket 3

# PREDICT: If I forgot the break statement, the loop would never end.

while True:
    user_input = input("Enter an age or type 'stop': ")
    if user_input == "stop":
        break
    age = int(user_input)
    if age >= 13:
        print("Access granted")
    else:
        print("Too young")

# EXPLAIN:
# Ticket 2 repeats while the answer is "yes."
# Ticket 3 repeats forever until the user types "stop" and break ends the loop.

# Ticket 4

# PREDICT:
# The output will be the same as Ticket 1, but the function does the age check instead of writing the if/else each time.

def can_access(age):
    if age >= 13:
        return True
    else:
        return False

ages = [17, 11, 25, 13, 9]
for age in ages:
    if can_access(age):
        print(f"{age} — Access granted")
    else:
        print(f"{age} — Too young")

# EXPLAIN:
# A function lets us reuse the same code instead of writing the same one if/else over and over.

# Ticket 5

# PREDICT:
# --- StreamPass Signup Report ---
# Signup #1 | Age 22 — Access granted
# Signup #2 | Age 10 — Too young 
# Signup #3 | Age 15 — Access granted 
# Signup #4 | Age 8 — Too young 
# Signup #5 | Age 19 — Access granted 
# Signup #6 | Age 13 — Access granted 
# Approved: 4 out of 6

def signup_report(ages):
    approved = 0

    print("--- StreamPass Signup Report ---")
    for number, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young")

    print(f"Approved: {approved} out of {len(ages)}")


signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)

# EXPLAIN:
# I used functions, parameters, return, a for loop, enumerate(), if/else statements,
# variables, a counter, and a list.
