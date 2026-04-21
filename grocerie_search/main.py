from backend.grocery_service import search_item


def main() -> None:
    result = search_item("milk")

    print(result)


if __name__ == "__main__":
    main()
