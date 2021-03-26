class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, costumer, order, day):
        self.data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_dishes_counter = dict()

        for order in self.data:
            if order[0] == costumer:
                if order[1] not in costumer_dishes_counter:
                    costumer_dishes_counter[order[1]] = 1
                else:
                    costumer_dishes_counter[order[1]] += 1

        return max(costumer_dishes_counter, key=costumer_dishes_counter.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        costumer_order_counter = 0

        for order in self.data:
            if order[0] == costumer and order[1] == order:
                costumer_order_counter += 1

        return costumer_order_counter

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        costumer_dishes_ordered = set()

        for order in self.data:
            if order[1] not in all_dishes:
                all_dishes.add(order[1])
            if order[0] == costumer and order[1] \
               not in costumer_dishes_ordered:
                costumer_dishes_ordered.add(order[1])

        costumer_not_ordered = all_dishes - costumer_dishes_ordered

        return costumer_not_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days_went = set()

        for order in self.data:
            if order[2] not in all_days:
                all_days.add(order[2])
            if order[0] == costumer and order[2] not in costumer_days_went:
                costumer_days_went.add(order[2])

        costumer_not_went = all_days - costumer_days_went

        return costumer_not_went

    def get_busiest_day(self):
        days_counter = dict()

        for order in self.data:
            if order[2] not in days_counter:
                days_counter[order[2]] = 1
            else:
                days_counter[order[2]] += 1

        return max(days_counter, key=days_counter.get)

    def get_least_busy_day(self):
        days_counter = dict()

        for order in self.data:
            if order[2] not in days_counter:
                days_counter[order[2]] = 1
            else:
                days_counter[order[2]] += 1

        return min(days_counter, key=days_counter.get)
