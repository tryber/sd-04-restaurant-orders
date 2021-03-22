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
        pedidos_lanche = defaultdict(int)

        for order in self.orders:
            if order[0] == costumer:
                pedidos_lanche[order[1]] += 1

        return max(pedidos_lanche, key=pedidos_lanche.get)

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

        day_clients = set()
        todos_os_dias = set()

        for order in self.orders:
            todos_os_dias.add(order[2])

        for order in self.orders:
            if order[0] == costumer:
                day_clients.add(order[2])

        return todos_os_dias.difference(day_clients)

    def get_busiest_day(self):
        if len(self.orders) == 0:
            return None
        dias = defaultdict(int)
        for order in self.orders:
            dias[order[2]] += 1

        return max(dias, key=dias.get)

    def get_least_busy_day(self):
        if len(self.orders) == 0:
            return None
        dias = defaultdict(int)
        for order in self.orders:
            dias[order[2]] += 1

        return min(dias, key=dias.get)
