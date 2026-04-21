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


def find_cheapest_store(prices):
    cheapest_store = None
    cheapest_price = None

    for store, price in data["prices"].items():
        if cheapest_price is None or price < cheapest_price:
            cheapest_store = store
            cheapest_price = price

    return cheapest_store


def search_item(item_name):
    cheapest_store = find_cheapest_store(data["prices"])

    return {
        "item": item_name,
        "cheapest_store": cheapest_store,
        "prices": {
            "Aldi": 3.75,
            "Walmart": 4.12,
            "Commissary": 3.89,
        },
    }
