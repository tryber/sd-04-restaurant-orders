from src.analyze_log import never_go
from src.analyze_log import never_ordered


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        order = [costumer, order, day]
        self.orders.append(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = {}
        for name, food, day in self.orders:
            if name == costumer:
                if food not in orders:
                    orders[food] = 1
                else:
                    orders[food] += 1
        return max(orders, key=orders.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        count = 0
        for name, food, day in self.orders:
            if name == costumer and food == order:
                count += 1
        return count

    def get_never_ordered_per_costumer(self, costumer):
        result = never_ordered(self.orders, costumer)
        return result

    def get_days_never_visited_per_costumer(self, costumer):
        result = never_go(self.orders, costumer)
        return result

    def get_busiest_day(self):
        days_visited = {}

        for name, food, day in self.orders:
            if day is not days_visited:
                days_visited[day] = 1
            else:
                days_visited[day] += 1
        return max(days_visited, key=days_visited.get)

    def get_least_busy_day(self):
        days_visited = {}

        for name, food, day in self.orders:
            if day is not days_visited:
                days_visited[day] = 1
            else:
                days_visited[day] += 1
        return min(days_visited, key=days_visited.get)
