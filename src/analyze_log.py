from src.track_orders import TrackOrders
import csv


def restaurant_orders(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    with open(path_to_file, encoding="utf-8") as file:
        data_list = list(csv.reader(file))

    orders = TrackOrders()

    for name, dish, weekday in data_list:
        orders.add_new_order(name, dish, weekday)

    return orders


def analyze_log(path_to_file):
    order = restaurant_orders(path_to_file)
    costumers = [
        order.get_most_ordered_dish_per_costumer("maria"),
        order.get_order_frequency_per_costumer("arnaldo", "hamburguer"),
        order.get_never_ordered_per_costumer("joao"),
        order.get_days_never_visited_per_costumer("joao")
    ]

    with open('data/mkt_campaign.txt', "w", encoding="utf-8") as file:
        for costumer in costumers:
            file.write(f"{costumer}\n")
