# nested loop = a loop within another loop

rows = int(input("Enter the # of rows to use: "))
columns = int(input("Enter the # of columns to use: "))
symbol = input("Enter the symbol you would like to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
