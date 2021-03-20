from collections import defaultdict
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = defaultdict(list)
        self.foods = set()
        
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders[costumer].append([order, day])
        self.foods.add(order)
        
    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_most_ordered = Counter(self.orders[costumer][0])
        return list(costumer_most_ordered.keys())[0]

    def get_order_frequency_per_costumer(self, costumer, order):
       pass

    def get_never_ordered_per_costumer(self, costumer):
        costumer_food = set()
        for item in self.orders[costumer]:
            costumer_food.add(item[0])
        return self.foods.difference(costumer_food)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
