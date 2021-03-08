import csv


def common_recipe(data, costumer):
    favorite_food = ""
    orders = {}

    for name, order, day in data:
        if name == costumer:
            if order not in orders:
                orders[order] = 1
            else:
                orders[order] += 1

            if (
                favorite_food not in orders
                or orders[order] > orders[favorite_food]
            ):
                favorite_food = order

    return favorite_food


def order_qty(data, costumer, recipe):
    quantity = 0

    for name, order, day in data:
        if name == costumer and order == recipe:
            quantity += 1

    return quantity


def unused_recipe(data, costumer):
    foods = set()
    costumer_foods = set()

    for name, order, day in data:
        foods.add(order)

        if name == costumer:
            costumer_foods.add(order)

    return foods.difference(costumer_foods)


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
