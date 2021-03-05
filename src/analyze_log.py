import csv


def common_recipe(data, costumer):
    most_requery = ""
    orders = {}

    for name, order, day in data:
        if name == costumer:
            if order not in orders:
                orders[order] = 1
            else:
                orders[order] += 1

            if (
                most_requery not in orders
                or orders[order] > orders[most_requery]
            ):
                most_requery = order

    return most_requery


def order_qty(data, costumer, recipe):
    quantity = 0

    for name, order, day in data:
        if name == costumer and order == recipe:
            quantity += 1

    return quantity


def unused_recipe(data, costumer):
    recipes = set()
    costumer_recipes = set()

    for name, order, day in data:
        recipes.add(order)

        if name == costumer:
            costumer_recipes.add(order)

    return recipes.difference(costumer_recipes)


def days_off(data, costumer):
    days_on = set()
    days_with_people = set()

    for name, order, day in data:
        days_on.add(day)

        if name == costumer:
            days_with_people.add(day)

    return days_on.difference(days_with_people)


def analyze_log(path_to_file):
    with open(path_to_file, "r") as orders_file:
        content = csv.reader(orders_file, delimiter=",")
        data = [*content]

        common_recipe_save = common_recipe(data, "maria")
        order_qty_save = order_qty(
            data, "arnaldo", "hamburguer"
        )
        unused_recipe_save = unused_recipe(data, "joao")
        days_off_save = days_off(data, "joao")

        with open("data/mkt_campaign.txt", "w") as marketing_list:
            print(
                common_recipe_save,
                order_qty_save,
                unused_recipe_save,
                days_off_save,
                sep="\n",
                file=marketing_list,
            )
