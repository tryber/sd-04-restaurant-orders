# from analyze_log import ordered_dish_per_costumer
# from analyze_log import order_frequency_per_costumer
from collections import defaultdict


class TrackOrders:

    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque, e inicia em len 0
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None
        ordered_dish = defaultdict(int)
        for order in self.orders:
            if order[0] == costumer:
                ordered_dish[order[1]] += 1
        result = dict(ordered_dish)
        return max(result, key=result.get)

    # def get_order_frequency_per_costumer(self, costumer, order):
    #     pass

    def get_dishes(self):
        dishes = set()
        for order in self.orders:
            dishes.add(order[1])
        return dishes

    def get_never_ordered_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None
        ordered = set()
        dishes = self.get_dishes()
        for order in self.orders:
            if order[0] == costumer:
                ordered.add(order[1])
        return dishes.difference(ordered)

    # def get_days_never_visited_per_costumer(self, costumer):
    #     pass

    # def get_busiest_day(self):
    #     pass

    # def get_least_busy_day(self):
    #     pass
