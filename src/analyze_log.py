import csv
import operator


def get_favorite_orders(data, client):
    client_orders = {}

    for name, food, day in data:
        if client == name:
            if food not in client_orders:
                client_orders[food] = 1
            else:
                client_orders[food] += 1

    return max(client_orders.items(), key=operator.itemgetter(1))[0]


def order_times_ordered(data, client, ordered):
    times = 0

    for name, food, day in data:
        if client == name and ordered == food:
            times += 1

    return times


def get_not_ordered(data, client):
    all_foods = set()
    client_orders = set()

    for name, food, day in data:
        all_foods.add(food)

        if client == name:
            client_orders.add(food)

    return all_foods.difference(client_orders)


def get_days_client_gone(data, client):
    all_days = set()
    gone_days = set()

    for name, food, day in data:
        all_days.add(day)

        if client == name:
            gone_days.add(day)

    return all_days.difference(gone_days)


def analyze_log(path_to_file):
    with open(path_to_file, "r") as file:
        content = csv.reader(file, delimiter=",")
        data = [*content]

    with open("data/mkt_campaign.txt", "w") as analyze_file:
        analyze_file.write(
            f"{get_favorite_orders(data, 'maria')}\n"
            )
        analyze_file.write(
            f"{order_times_ordered(data, 'arnaldo', 'hamburguer')}\n"
            )
        analyze_file.write(f"{get_not_ordered(data, 'joao')}\n")
        analyze_file.write(f"{get_days_client_gone(data, 'joao')}\n")
