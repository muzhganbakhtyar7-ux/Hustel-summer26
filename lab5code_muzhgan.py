#Snippet 1
#Error type: ZeroDivisionError

x = 10
y = 2
result = x / y
print("Result:", result)
#output: Result: 5.0

#Snippet 2
#Error type: IndexError

numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])

#output: 1,2,3,4,5.

#Snippet 3
#Error type: SyntaxError

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

#output:78.5

#Snippet 4
#Error type: SyntaxError

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

#output: True, False

#Snippet 5
#Error type: SyntaxError

for i in range(5):
    print(i)

#output: 0,1,2,3,4

#Snippet 6
#Error type: SyntaxError

def greet(name):
    return "Hello, " + name

print(greet("Alice"))

#output: Hello, Alice

#Snippet 7
#Error type: IndentationError

numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)

#output: sum of numbres: 15

#Snippet 8
#Error type: RecursionError

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#output: 120

#Snippet 9
#Error type: Logic Error

name = input("Enter your name: ")

if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

#output: Hello, Alice if your name is Alice.

#Snippet 10
#Error type: ZeroDivisionError

def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero."
    result = x / y
    return result

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))

#output: Cannot divide by zero.

