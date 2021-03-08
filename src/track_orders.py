
from src.analyze_log import count_customer_habits
from src.analyze_log import count_customer_habits_set


class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return count_customer_habits(costumer, 'food', self.orders)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return count_customer_habits_set(costumer, 'food', self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return count_customer_habits_set(costumer, 'weekday', self.orders)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
