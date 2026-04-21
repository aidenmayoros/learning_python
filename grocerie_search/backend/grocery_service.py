"""Grocery search and price comparison logic will go here."""

# Fake Database data
data = {
    "item": "milk",
    "cheapest_store": "Aldi",
    "prices": {
        "Aldi": 3.75,
        "Walmart": 4.12,
        "Commissary": 3.89,
    },
}


def search_item(item_name):
    return {
        "item": item_name,
        "cheapest_store": "Aldi",
        "prices": {
            "Aldi": 3.75,
            "Walmart": 4.12,
            "Commisary": 3.89,
        },
    }
