# a collection of {key: value} pairs - ordered and changeable but no duplicates

capitals = {
    "USA": "Washington D.C",
    "India": "New Delhii",
    "China": "Beijing",
    "Russia": "Moscow",
}

# Methods

# Gets the value of key or None if there is no key
print(capitals.get("USA"))  # returns Washington D.C

# Add or change
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "The World"})

# Remove key and value
capitals.pop("China")

# Show all keys in a list [] can do the same thing with the values method
keys = capitals.keys()

print(capitals)
