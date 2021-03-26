class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'costumer': costumer,
            'order': order,
            'day': day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered_dishs = [
            order['order']
            for order in self.orders
            if order['costumer'] == costumer
        ]

        return max(ordered_dishs, key=ordered_dishs.count)

    def get_order_frequency_per_costumer(self, costumer, order):
        ordered_dishs = [
            order['order']
            for order in self.orders
            if order['costumer'] == costumer and order['order'] == order
        ]

        return len(ordered_dishs)

    def no_orders(self, field, costumer):
        avaible = set([data[field] for data in self.orders])
        have_orders = set([
            data[field]
            for data in self.orders if data['costumer'] == costumer
        ])
        no_ordered = avaible.difference(have_orders)

        return no_ordered

    def get_never_ordered_per_costumer(self, costumer):
        return self.no_orders('order', costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return self.no_orders('day', costumer)

    def get_busiest_day(self):
        days = [
            order['day']
            for order in self.orders
        ]
        print(days)

        return max(days, key=days.count)

    def get_least_busy_day(self):
        days = [
            order['day']
            for order in self.orders
        ]

        return min(days, key=days.count)
