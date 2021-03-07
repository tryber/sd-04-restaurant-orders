import csv
from collections import Counter


def csv_importer():
    orders_list = list()
    with open("data/orders_1.csv") as csv_file:
        reader = csv.reader(csv_file)
        for costumer, order, day in reader:
            orders_list.append([costumer, order, day])
    csv_file.close()
    return orders_list


class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders_list = list()
        for name, order, day in csv_importer():
            if name == costumer:
                costumer_orders_list.append(order)
        return list(Counter(costumer_orders_list))[0]

    def get_order_frequency_per_costumer(self, costumer, order):
        costumer_orders_list = list()
        for name, order, day in csv_importer():
            if name == costumer:
                costumer_orders_list.append(order)
        return dict(Counter(costumer_orders_list))[order]

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        costumer_orders = set()

        for name, order, day in csv_importer():
            all_orders.add(order)
            if name == costumer:
                costumer_orders.add(order)

        return all_orders - costumer_orders

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days = set()

        for name, order, day in csv_importer():
            all_days.add(day)
            if name == costumer:
                costumer_days.add(day)

        return all_days - costumer_days

    def get_busiest_day(self):
        all_days = list()

        for name, order, day in self.orders:
            all_days.append(day)

        return list(Counter(all_days))[0]

    def get_least_busy_day(self):
        all_days = list()

        for name, order, day in self.orders:
            all_days.append(day)

        return list(Counter(all_days))[-1]
