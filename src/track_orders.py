from collections import defaultdict


class TrackOrders:
    def __init__(self, orders=None):
        self.orders = orders if orders is not None else list()

    def __len__(self):
        return len(self.orders)

    def get_dishes(self):
        if len(self.orders) == 0:
            return None
        dishes = set()
        for order in self.orders:
            dishes.add(order[1])
        return dishes

    def get_working_days(self):
        if len(self.orders) == 0:
            return None
        working_days = set()
        for order in self.orders:
            working_days.add(order[2])
        return working_days

    def get_days_frequencies(self):
        if len(self.orders) == 0:
            return None
        days_of_the_week = defaultdict(int)
        for order in self.orders:
            days_of_the_week[order[2]] += 1
        return dict(days_of_the_week)

    def get_dish_count_by_person(self, costumer, dish):
        dish_count = 0
        for order in self.orders:
            if order[0] == costumer and order[1] == dish:
                dish_count += 1
        return dish_count

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None
        ordered_dishes = defaultdict(int)
        for order in self.orders:
            if order[0] == costumer:
                ordered_dishes[order[1]] += 1
        ordered_dishes_result = dict(ordered_dishes)
        return max(ordered_dishes_result, key=ordered_dishes_result.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None
        ordered = set()
        dishes = self.get_dishes()
        for order in self.orders:
            if order[0] == costumer:
                ordered.add(order[1])
        return dishes.difference(ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None
        working_days = self.get_working_days()
        days_went = set()
        for order in self.orders:
            if order[0] == costumer:
                days_went.add(order[2])
        return working_days.difference(days_went)

    def get_busiest_day(self):
        if len(self.orders) == 0:
            return None
        days = self.get_days_frequencies()
        return max(days, key=days.get)

    def get_least_busy_day(self):
        if len(self.orders) == 0:
            return None
        days = self.get_days_frequencies()
        return min(days, key=days.get)
