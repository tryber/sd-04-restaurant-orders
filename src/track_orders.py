class TrackOrders:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def add_new_order(self, costumer, order, day):
        return self._data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered = {}
        for item in self._data:
            food = item[1]
            if item[0] == costumer:
                if food not in ordered:
                    ordered[food] = 1
                else:
                    ordered[food] += 1
        order = max(ordered, key=ordered.get)
        return order

    def get_order_frequency_per_costumer(self, costumer, order):
        count = 0
        for item in self._data:
            if item[0] == costumer:
                if item[1] == order:
                    count += 1
        return count

    def get_never_ordered_per_costumer(self, costumer):
        original = set()
        modified = set()

        for order in self._data:
            original.add(order[1])
            if (order[0]) == costumer:
                modified.add(order[1])
        diff = original.difference(modified)
        return diff

    def get_days_never_visited_per_costumer(self, costumer):
        original = set()
        modified = set()

        for order in self._data:
            original.add(order[2])
            if (order[0]) == costumer:
                modified.add(order[2])

        diff = original.difference(modified)
        return diff

    def get_busiest_day(self):
        days = {}
        for item in self._data:
            day = item[2]
            if day not in days:
                days[day] = 1
            else:
                days[day] += 1
        most_busy = max(days, key=days.get)
        return most_busy

    def get_least_busy_day(self):
        days = {}
        for item in self._data:
            day = item[2]
            if day not in days:
                days[day] = 1
            else:
                days[day] += 1
        most_busy = min(days, key=days.get)
        return most_busy
