# input() a function to prompt the user for data and returns the response as a string.

name = input("What is your name? ")

age = input("How old are you? ")

# To run arythmatic on user input we need to typecast it to int or float
# You can do it on the print statement or on the input function either will work
# int(input("How old are you? "))
print(f"Your age plus one is {int(age) + 1}")

print(f"Hello {name}")
