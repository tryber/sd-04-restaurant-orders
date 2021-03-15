from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        cust_order = []
        for cust_name, rango, _ in self.orders:
            if cust_name == costumer:
                cust_order.append([cust_name, rango])

        resp = Counter([order[1] for order in cust_order])
        return resp.most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set([order[1] for order in self.orders])
        cust_dishes = set(
            [order[1] for order in self.orders if order[0] == costumer]
        )

        return dishes - cust_dishes

    def get_days_never_visited_per_costumer(self, costumer):
        days = set([order[2] for order in self.orders])
        cust_days = set(
            [order[2] for order in self.orders if order[0] == costumer]
        )

        return days - cust_days

    def get_busiest_day(self):
        days = Counter([order[2] for order in self.orders])

        return days.most_common(1)[0][0]

    def get_least_busy_day(self):
        days = Counter([order[2] for order in self.orders])

        return days.most_common(3)[2][0]
