class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_requery = ""
        orders = {}

        for name, order, day in self.orders:
            if name == costumer:
                if order not in orders:
                    orders[order] = 1
                else:
                    orders[order] += 1

                if (
                    most_requery not in orders
                    or orders[order] > orders[most_requery]
                ):
                    most_requery = order

        return most_requery

    def get_order_frequency_per_costumer(self, costumer, order):
        quantity = 0

        for name, recipe, day in self.orders:
            if name == costumer and recipe == order:
                quantity += 1

        return quantity

    def get_never_ordered_per_costumer(self, costumer):
        recipes = set()
        costumer_recipes = set()

        for name, order, day in self.orders:
            recipes.add(order)

            if name == costumer:
                costumer_recipes.add(order)

        return recipes.difference(costumer_recipes)

    def get_days_never_visited_per_costumer(self, costumer):
        days_on = set()
        days_with_people = set()

        for name, order, day in self.orders:
            days_on.add(day)

            if name == costumer:
                days_with_people.add(day)

        return days_on.difference(days_with_people)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

