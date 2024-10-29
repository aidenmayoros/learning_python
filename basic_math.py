import math

# Basic operators
# -----------------------
friends = 0

# friends = friends + 1
# friends += 1
# friends -= 1
# friends *= 2
# friends /= 2
# friends **= 2
# friends = friends % 2

# print(friends)

# Built in math functions
# ----------------------

x = 3.14
y = -4
z = 5

round(x)  # returns 3
abs(y)  # returns 4 - distance from 0
pow(4, 3)  # returns 64 - 4 x 4 x 4 or 4 to power of 3
max(x, y, z)  # returns maximum value of given numbers - 5
min(x, y, z)  # returns minimum value of given numbers - -4

# Math Module
# import math - at top level of file
# ----------------------

math.pi
math.e
math.sqrt(x)  # find square root
math.ceil(y)  # round up
math.floor(y)  # round down

# If statements
# ----------------------

# age = int(input("What is your age? "))

# if age >= 18:
#     print("You are signed up!")
# elif age < 0:
#     print("You have not been born yet!")
# else:
#     print("You must be 18 to sign up!")

# Second example
# -----------------------

# food_question = input("Would you like some food? Y/N ")

# if food_question == "Y":
#     print("Enjoy!")
# else:
#     print("No food for you!")\

# Python Calculator
# -----------------------

operator = input("Choose a operator (+ - * /) ")
num1 = float(input("Enter 1st number "))
num2 = float(input("Enter 2nd number "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Please choose only one of the following operators (+ - * /)")
