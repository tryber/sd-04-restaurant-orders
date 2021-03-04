import csv
from src.track_orders import TrackOrders


# class TrackOrders:
#     def __init__(self, orders, customer_name):
#         self.orders = orders
#         self.customer_name = customer_name

#     def get_working_days(self):
#         working_days = set()
#         for order in self.orders:
#             working_days.add(order[2])
#         return working_days

#     def get_dishes(self):
#         dishes = set()
#         for order in self.orders:
#             dishes.add(order[1])
#         return dishes

#     def get_most_ordered_dish(self):
#         ordered_dishes = defaultdict(int)
#         for order in self.orders:
#             if order[0] == self.customer_name:
#                 ordered_dishes[order[1]] += 1
#         ordered_dishes_result = dict(ordered_dishes)
#         return max(ordered_dishes_result, key=ordered_dishes_result.get)

#     def get_dish_count_by_person(self, dish):
#         dish_count = 0
#         for order in self.orders:
#             if order[0] == self.customer_name and order[1] == dish:
#                 dish_count += 1
#         return dish_count

#     def get_never_ordered_by_person(self):
#         ordered = set()
#         dishes = self.get_dishes()
#         for order in self.orders:
#             if order[0] == self.customer_name:
#                 ordered.add(order[1])
#         return dishes.difference(ordered)

#     def get_never_went_by_person(self):
#         working_days = self.get_working_days()
#         days_went = set()
#         for order in self.orders:
#             if order[0] == self.customer_name:
#                 days_went.add(order[2])
#         return working_days.difference(days_went)


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
        # maria_orders = TrackOrders(orders, "maria")
        # arnaldo_orders = TrackOrders(orders, "arnaldo")
        # joao_orders = TrackOrders(orders, "joao")
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
