from src.analyze_log import best_seller_by_client
from src.analyze_log import favorite_dish_by_client
from src.analyze_log import never_ordered
from src.analyze_log import never_be_in_day
from src.analyze_log import get_total_dish
from src.analyze_log import get_total_days


class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.dishes = set()
        self.days = set()
        self.count = {}
        self.list_of_days = list()
        self.most_frequent = ""
        self.last_frequent = ""

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = [(order, day)]
        else:
            self.orders[costumer].append((order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return best_seller_by_client(costumer, self.orders)

    def get_order_frequency_per_costumer(self, costumer, order):
        return favorite_dish_by_client(costumer, order, self.orders)

    def get_never_ordered_per_costumer(self, costumer):
        self.dishes = get_total_dish(self.orders)
        return never_ordered(costumer, self.dishes, self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        self.days = get_total_days(self.orders)
        return never_be_in_day(costumer, self.days, self.orders)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
