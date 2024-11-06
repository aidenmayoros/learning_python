# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to 0")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to 0")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to 0")
