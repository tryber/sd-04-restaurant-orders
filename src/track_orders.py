from collections import defaultdict


class TrackOrders:

    def __init__(self):
        self.orders = list()

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

        return max(ordered_dish, key=ordered_dish.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None
        ordered = set()
        dishes = set()
        for order in self.orders:
            dishes.add(order[1])

        for order in self.orders:
            if order[0] == costumer:
                ordered.add(order[1])

        return dishes.difference(ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        if len(self.orders) == 0:
            return None

        visited_days = set()
        all_days = set()

        for order in self.orders:
            all_days.add(order[2])

        for order in self.orders:
            if order[0] == costumer:
                visited_days.add(order[2])

        return all_days.difference(visited_days)

    def get_busiest_day(self):
        if len(self.orders) == 0:
            return None
        days = defaultdict(int)
        for order in self.orders:
            days[order[2]] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        if len(self.orders) == 0:
            return None
        days = defaultdict(int)
        for order in self.orders:
            days[order[2]] += 1

        return min(days, key=days.get)
