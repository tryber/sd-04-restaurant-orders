class TrackOrders:
    def __init__(self):
        self.list_orders = []

    def __len__(self):
        return len(self.list_orders)

    def add_new_order(self, costumer, order, day):
        '''add novo pedido'''
        self.list_orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        ''' retornar o prato mais pedido'''
        favorite_recipe = ""
        obj_orders = {}

        for name, order, day in self.list_orders:
            if name == costumer:
                if order not in obj_orders:
                    obj_orders[order] = 1
                else:
                    obj_orders[order] += 1

                if (
                    favorite_recipe not in obj_orders
                    or obj_orders[order] > obj_orders[favorite_recipe]
                ):
                    favorite_recipe = order

        return favorite_recipe

    def get_order_frequency_per_costumer(self, costumer, order):
        qty = 0

        for name, day, recipe in self.list_orders:
            if name == costumer and recipe == order:
                qty += 1

        return qty

    def get_never_ordered_per_costumer(self, costumer):
        recipes = set()
        client_recipes = set()

        for name, order, day in self.list_orders:
            recipes.add(order)

            if name == costumer:
                client_recipes.add(order)

        return recipes.difference(client_recipes)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        client_visited = set()

        for name, order, day in self.list_orders:
            days.add(day)

            if name == costumer:
                client_visited.add(day)

        return days.difference(client_visited)

    def get_busiest_day(self):
        busiest_day = list(self.list_orders.keys())[0]

        for day in self.list_orders:
            if self.list_orders[day] > self.list_orders[busiest_day]:
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        pass
