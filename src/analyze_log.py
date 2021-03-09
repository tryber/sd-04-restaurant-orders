import csv

def most_requested_recipe(orders, costumer):
    favorite = ""
    orders = {}

    for name, order, day in orders:
        if name == costumer:
            if order not in orders:
                orders[order] = 1
            else:
                orders[order] += 1

            if (
                favorite not in orders
                or orders[order] > orders[favorite]
            ):
                favorite = order

    return favorite


def quantity_orders(orders, costumer, product):
    quantity = 0
    for order in orders[costumer]:
        if order["product"] == product:
            quantity += 1
    return quantity


def not_ordered(orders, costumer):
    products_costumers = set()
    products = set()

    for name, order, day in orders:
        products.add(order)

        if name == costumer:
            products_costumers.add(order)

    return products.difference(products_costumers)


def not_visited(orders, costumer):
    days = set()
    visited_days = set()

    for name, order, day in orders:
        days.add(day)

        if name == costumer:
            visited_days.add(day)

    return days.difference(visited_days)


def analyze_log(path_to_file):
    with open(path_to_file, "r") as orders_file:
        orders_reader = csv.reader(orders_file, delimiter=",")
        orders = [*orders_reader]

        most_requested_recipe_save = most_requested_recipe(orders, "maria")
        quantity_orders_save = quantity_orders(
            orders, "arnaldo", "hamburguer"
        )
        not_ordered_save = not_ordered(orders, "joao")
        not_visited_save = not_visited(orders, "joao")

        with open("data/mkt_campaign.txt", "w") as marketing_list:
            print(
                most_requested_recipe_save,
                quantity_orders_save,
                not_ordered_save,
                not_visited_save,
                sep="\n",
                file=marketing_list,
            )