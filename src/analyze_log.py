import csv
from src.track_orders import TrackOrders

def analyze_log(path_to_file):

    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(
                "No such file or directory: " f"'{path_to_file}'"
            )

    orders = list()

    with open(path_to_file) as file:
        orders_reader = csv.reader(file, delimiter=",")
        for order in orders_reader:
            orders.append(order)

        file.close()

    with open("data/mkt_campaign.txt", "w") as result_file:
        orders_tracker = TrackOrders(orders)

        result_file.write(
            orders_tracker.get_most_ordered_dish_per_costumer("maria") + "\n"
        )
        result_file.write(
            str(
                orders_tracker.get_dish_count_by_person(
                    "arnaldo", "hamburguer"
                )
            )
            + "\n"
        )
        result_file.write(
            str(orders_tracker.get_never_ordered_per_costumer("joao")) + "\n"
        )
        result_file.write(
            str(orders_tracker.get_days_never_visited_per_costumer("joao"))
            + "\n"
        )

        result_file.close()