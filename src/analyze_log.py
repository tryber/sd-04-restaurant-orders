import csv


def most_requested_recipe(total_orders, costumer):
    most_requested = ""
    orders = {}

    for name, order, day in total_orders:
        if name == costumer:
            if order not in orders:
                orders[order] = 1
            else:
                orders[order] += 1

            if (
                most_requested not in orders
                or orders[most_requested] < orders[order]
            ):
                most_requested = order

    return most_requested


def quantity_orders(orders, costumer, product):
    total_quantity = 0

    for name, order, day in orders:
        if name == costumer and order == product:
            total_quantity += 1

    return total_quantity


def not_ordered(orders, costumer):
    products_costumers = set()
    products = set()

    for name, order, day in orders:
        products.add(order)
        if name == costumer:
            products_costumers.add(order)

    result = products.difference(products_costumers)
    return result


def not_visited(orders, costumer):
    days = set()
    visited_days = set()

    for name, order, day in orders:
        days.add(day)

        if name == costumer:
            visited_days.add(day)

    result = days.difference(visited_days)
    return result


def analyze_log(path_to_file):
    with open(path_to_file, "r") as orders_file:
        orders = [*csv.reader(orders_file, delimiter=",")]
        most_requested_recipe_final = most_requested_recipe(orders, "maria")
        quantity_orders_final = quantity_orders(
            orders, "arnaldo", "hamburguer"
        )
        not_ordered_final = not_ordered(orders, "joao")
        not_visited_final = not_visited(orders, "joao")

        with open("data/mkt_campaign.txt", "w") as marketing_list:
            print(
                most_requested_recipe_final,
                quantity_orders_final,
                not_ordered_final,
                not_visited_final,
                sep="\n",
                file=marketing_list,
            )
