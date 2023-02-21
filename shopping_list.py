# Assignment A_10 Shopping list

from shopping_module import *


def menu_options():
    option = input("What do you want to do? \n1. Add to list \n2. Print shopping list \n3. Empty shopping list")
    if option == "1":
        add_products_to_shopping_list()
    if option == "2":
        print_shopping_list()
    if option == "3":
        empty_shopping_list()
    menu_options()


def add_products_to_shopping_list():
    product = input("What product do you want to buy?")
    number_of_product = input("How many do you want to buy?")
    save_to_list(product, number_of_product)


def empty_shopping_list():
    clear_list()


menu_options()
