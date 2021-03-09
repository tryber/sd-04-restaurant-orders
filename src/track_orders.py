class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_requested = ""
        orders = {}

        for name, order, day in self.orders:
            if name == costumer:
                if order not in orders:
                    orders[order] = 1
                else:
                    orders[order] += 1

                if (
                    most_requested not in orders
                    or orders[most_requested] < orders[order]
                ):
                    most_requested = order

        return most_requested

    def get_order_frequency_per_costumer(self, costumer, order):
        total_quantity = 0

        for name, order, day in self.orders:
            if name == costumer and order == order:
                total_quantity += 1

        return total_quantity

    def get_never_ordered_per_costumer(self, costumer):
        products_costumers = set()
        products = set()

        for name, order, day in self.orders:
            products.add(order)
            if name == costumer:
                products_costumers.add(order)

        result = products.difference(products_costumers)
        return result

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        visited_days = set()

        for name, order, day in self.orders:
            days.add(day)

            if name == costumer:
                visited_days.add(day)

        result = days.difference(visited_days)
        return result

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
