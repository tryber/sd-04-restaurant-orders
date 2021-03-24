from src.analyze_log import get_favorite_orders
from src.analyze_log import order_times_ordered
from src.analyze_log import get_not_ordered
from src.analyze_log import get_days_client_gone
import operator


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_favorite_orders(self.orders, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return order_times_ordered(self.orders, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return get_not_ordered(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return get_days_client_gone(self.orders, costumer)

    def get_busiest_day(self):
        visited_days = {}

        for name, food, day in self.orders:
            if day not in visited_days:
                visited_days[day] = 1
            else:
                visited_days[day] += 1

        return max(visited_days.items(), key=operator.itemgetter(1))[0]

    def get_least_busy_day(self):
        visited_days = {}

        for name, food, day in self.orders:
            if day not in visited_days:
                visited_days[day] = 1
            else:
                visited_days[day] += 1

        return min(visited_days.items(), key=operator.itemgetter(1))[0]
