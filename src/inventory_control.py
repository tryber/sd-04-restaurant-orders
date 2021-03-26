from src.analyze_log import favorite_recipe
from src.analyze_log import qty_orders
from src.analyze_log import not_orders


class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.products = set()
        self.days_of_week = set()
        self.orders_per_day = {}
        self.lenght = 0

    def __len__(self):
        return self.lenght

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = [
                {"product": order, "days_of_week": day}
            ]
        else:
            self.orders[costumer].append(
                {"product": order, "days_of_week": day}
            )

        self.lenght += 1
        self.products.add(order)

        if day not in self.orders_per_day:
            self.orders_per_day[day] = 1
        else:
            self.orders_per_day[day] += 1
        self.days_of_week.add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return favorite_recipe(self.orders, costumer)

    def get_dish_quantity_per_costumer(self, costumer, order):
        return qty_orders(self.orders, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return not_orders(self.orders, costumer, self.products, "product")

    def get_busiest_day(self):
        frequency = list(self.orders_per_day.keys())[0]

        for day in self.orders_per_day:
            if self.orders_per_day[day] > self.orders_per_day[frequencia]:
                frequency = day

        return frequency

    def get_least_busy_day(self):
        frequency = list(self.orders_per_day.keys())[0]

        for day in self.orders_per_day:
            if self.orders_per_day[day] < self.orders_per_day[frequencia]:
                frequency = day

        return frequency
