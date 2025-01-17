# Concession stand program for practce of dictionary

# Dictionary {key: value}

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 1.00,
    "fries": 3.00,
    "chips": 2.00,
    "pretzel": 1.50,
    "soda": 2.50,
}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10} ${value:.2f}")
