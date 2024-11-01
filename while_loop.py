# While loop will execute a block of code until the conditional is false

name = input("Please enter your name ")

while name == "":
    print("You did not enter your name")
    name = input("Please enter your name ")

print(f"Hello {name}")
