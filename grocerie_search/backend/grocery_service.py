import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_all_store_data():
    all_stores_data = {}

    for json_file in DATA_DIR.glob("*.json"):
        store_name = json_file.stem.replace("_prices", "")
        with json_file.open("r", encoding="utf-8") as file:
            all_stores_data[store_name] = json.load(file)

    return all_stores_data


def find_lowest_price_store(item_name):
    cheapest_store = None
    cheapest_price = None

    for store in data:
        print(store)
        for item, price in store:
            print(item)


data = load_all_store_data()
find_lowest_price_store("milk")
