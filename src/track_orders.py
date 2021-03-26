class TrackOrders:

    def __init__(self):
        self.orders = []


    def __len__(self):
        return len(self.orders)


    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])


    def get_most_ordered_dish_per_costumer(self, costumer):
        request = []
        bigger = set()
        for line in self.orders:
            if line[0] == costumer:
                request.append(line[1])
        for pedido in request:
            bigger.add((request.count(pedido), pedido))
            great_bigger = dict(bigger)
        return great_bigger[max(great_bigger)]


    def get_order_frequency_per_costumer(self, costumer, order):
        requested = []
        for line in self.orders:
            if line[0] == costumer:
                requested.append(line[1])
        return requested.count(order)


    def get_never_ordered_per_costumer(self, costumer):
        requested = set()
        request_user = set()
        for line in self.orders:
            if line[0] == costumer:
                request_user.add(line[1])
            else:
                requested.add(line[1])
        return requested - request_user


    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_user = set()
        for line in self.orders:
            if line[0] == costumer:
                days_user.add(line[2])
            else:
                days.add(line[2])
        return days - days_user


    def get_busiest_day(self):
        request = []
        bigger = set()
        for line in self.orders:
            request.append(line[2])
        for requested in request:
            bigger.add((request.count(requested), requested))
            great_bigger = dict(bigger)
        return great_bigger[max(great_bigger)]


    def get_least_busy_day(self):
        request = []
        bigger = set()
        for line in self.orders:
            request.append(line[2])
        for requested in request:
            bigger.add((request.count(requested), requested))
            great_bigger = dict(bigger)
        return great_bigger[min(great_bigger)]
        