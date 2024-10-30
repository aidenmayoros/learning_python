age = int(input("What is your age? "))

if age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You must be 18 to sign up!")

# -----------------------
# Second example
# -----------------------

food_question = input("Would you like some food? Y/N ")

if food_question == "Y":
    print("Enjoy!")
else:
    print("No food for you!")

# -----------------------
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
