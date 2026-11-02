# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
from random import random


fruits = ["apple", "banana", "orange"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = 5
while countdown >= 1:
    print(countdown)
    countdown -= 1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for number in range(1, 11):
    print(number ** 2)


#-------------------------------------------------------------------------

# Question 4: Using the random module

import random
import time


time.sleep(1)
print("Hello World")

# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]

# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print("Addition:", math_operations.add(10, 5))
print("Subtraction:", math_operations.subtract(10, 5))
print("Multiplication:", math_operations.multiply(10, 5))
print("Division:", math_operations.divide(10, 5))

# TODO: Use a while loop to create a simple calculator
operations = {
    "+": math_operations.add,
    "-": math_operations.subtract,
    "*": math_operations.multiply,
    "/": math_operations.divide,
}

while True:
    operation = input("Choose an operation (+, -, *, /) or q to quit: ").strip()
    if operation.lower() == "q":
        print("Calculator closed.")
        break

    if operation not in operations:
        print("Invalid operation. Choose +, -, *, /, or q.")
        continue

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    result = operations[operation](first_number, second_number)
    print("Result:", result)
