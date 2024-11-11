# Collection = single variable used to store multiple values.

# List = [] ordered and changable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangable. Duplicates OK FASTER

fruits = ["apple", "orange", "banana", "coconut"]
# lists have all kinds of methods like append, remove, insert, reverse, sort, pop, count and more - use google nerd

# You can get different data using a list
# print(fruits[0])
# print(fruits[:2])  # First 2
# print(fruits[::2])  # Every other 2
# print(fruits[::-1])  # All but reversed

# for fruit in fruits:
#     print(fruit)

# to find if a item is in collection do this returns boolean
# print("apple" in fruits)


set_of_fruits = {"apple", "orange", "banana", "coconut"}
# Sets have a lot of methods like a list

tuple_of_fruits = ("apple", "orange", "banana", "coconut")
# Tuples have some methods but not as many
