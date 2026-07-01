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