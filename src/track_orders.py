from src.analyze_log import get_food_most_requested_by_costumer
from src.analyze_log import get_foods_never_asked
from src.analyze_log import get_days_never_went

class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_food_most_requested_by_costumer(self.orders, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return get_foods_never_asked(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return get_days_never_went(self.orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
