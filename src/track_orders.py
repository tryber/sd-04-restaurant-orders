class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = {}
        most_ordered = self.orders[0][1]
        for order in self.orders:
            if order[0] == costumer:
                if order[1] in orders:
                    orders[order[1]] += 1
                else:
                    orders[order[1]] = 1

                if orders[order[1]] > orders[most_ordered]:
                    most_ordered = order[1]

        return most_ordered

    def get_order_frequency_per_costumer(self, costumer, order):
        quantity = 0
        for order in self.orders_list:
            if order[0] == costumer:
                if order[1] == order:
                    quantity += 1

        return quantity

    def get_never_ordered_per_costumer(self, costumer):
        products = set()
        ordered_products = set()

        for person, product, day in self.orders:
            products.add(product)
            if person == costumer:
                ordered_products.add(product)

        never_ordered_products = products.difference(ordered_products)
        return never_ordered_products

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        visited_days = set()

        for person, product, day in self.orders:
            days.add(day)
            if person == costumer:
                visited_days.add(day)

        never_visited_days = days.difference(visited_days)
        return never_visited_days

    def get_busiest_day(self):
        days = {}
        busiest_day = self.orders[0][2]
        for person, product, day in self.orders:
            if day in days:
                days[day] += 1
            else:
                days[day] = 1

            if days[day] > days[busiest_day]:
                busiest_day = days[day]

        return busiest_day

    def get_least_busy_day(self):
        days = {}
        least_busy_day = self.orders[0][2]
        for person, product, day in self.orders:
            if day in days:
                days[day] += 1
            else:
                days[day] = 1

            if days[day] <= days[least_busy_day]:
                least_busy_day = day

        return least_busy_day
