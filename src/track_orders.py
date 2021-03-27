class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        top_order = self.orders[0][1]
        for order in self.orders:
            if order[0] == costumer:
                if order[1] not in count:
                    count[order[1]] = 1
                else:
                    count[order[1]] += 1
                if count[order[1]] > count[top_order]:
                    top_order = order[1]
        return top_order

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        up = set()
        down = set()
        for order in self.orders:
            up.add(order[1])
            if order[0] == costumer:
                down.add(order[1])
        solution = up.difference(down)
        return solution

    def get_days_never_visited_per_costumer(self, costumer):
        up = set()
        down = set()
        for order in self.orders:
            up.add(order[2])
            if order[0] == costumer:
                down.add(order[2])
        solution = up.difference(down)
        return solution

    def get_busiest_day(self):
        count = {}
        busiest = self.orders[0][2]
        for order in self.orders:
            if order[2] not in count:
                count[order[2]] = 1
            else:
                count[order[2]] += 1

            if count[order[2]] > count[busiest]:
                busiest = count[order[2]]

        return busiest

    def get_least_busy_day(self):
        count = {}
        least = self.orders[0][2]
        for order in self.orders:
            if order[2] not in count:
                count[order[2]] = 1
            else:
                count[order[2]] += 1

            if count[order[2]] <= count[least]:
                least = order[2]

        return least
