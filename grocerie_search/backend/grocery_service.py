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


def find_all_store_prices(data):
    return


def search_item(item_name):
    cheapest_store = find_cheapest_store(data["prices"])
    prices = find_all_store_prices(data["prices"])

    return {
        "item": item_name,
        "cheapest_store": cheapest_store,
        "prices": prices,
    }
