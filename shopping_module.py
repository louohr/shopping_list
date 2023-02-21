# Assignment A_10 Shopping list.

shopping_dictionary = {}


def clear_list():
    print("Clearing shopping dictionary!")
    shopping_dictionary.clear()


def print_shopping_list():
    list_with_items = shopping_dictionary.items()
    print(sorted(list_with_items))


def save_to_list(item: str, number_of_item):
    print(f"Saving {number_of_item} {item} in the shopping list")
    shopping_dictionary.update({item: number_of_item})
