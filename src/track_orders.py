from collections import Counter

#  https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_order = []
        for c_name, food, _ in self.orders:
            if c_name == costumer:
                customer_order.append([c_name, food])

        result = Counter([order[1] for order in customer_order])
        return result.most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        food_orders = set([order[1] for order in self.orders])
        c_orders = set(
            [order[1] for order in self.orders if order[0] == costumer]
        )

        return food_orders - c_orders

    def get_days_never_visited_per_costumer(self, costumer):
        order_days = set([order[2] for order in self.orders])
        day_customer = set(
            [order[2] for order in self.orders if order[0] == costumer]
        )

        return order_days - day_customer

    def get_busiest_day(self):
        order_days = Counter([order[2] for order in self.orders])
        # list comprehension para contar os dias

        return order_days.most_common(1)[0][0]

    def get_least_busy_day(self):
        order_days = Counter([order[2] for order in self.orders])
        # list comprehension para contar os dias

        return order_days.most_common(3)[2][0]
        # vai retornar o mais comum entre o terceiro campo que é o de dia
