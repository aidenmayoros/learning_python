# -----------------------
# Common String Methods
# -----------------------

string_name = input("Enter your full name: ")

len(string_name)  # returns length of the string
string_name.find(" ")  # finds the first occurance and returns its position value
string_name.rfind(" ")  # finds the last occurance and returns its position value
string_name.capitalize()  # makes the first letter a capital
string_name.upper()  # Makes all letters uppercase
string_name.isdigit()  # checks if all string items are numbers
string_name.isalpha()  # checks for all alphabetical letters in a string
string_name.count()  # counts how many characters are in a string
string_name.replace()  # replaces all first parameter with another in a string

# -----------------------
# Validate user input
# 1. username must not be more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
# ------------------------------

username_input = input("Username: ")

if len(username_input) > 12:
    print("Username is too long, must be less than 12 characters")
elif not username_input.find(" "):
    print("Username must not contain spaces or white space")
elif not username_input.isalpha():
    print("Username must not contain numbers or special characters")
else:
    print("Username accepted")
