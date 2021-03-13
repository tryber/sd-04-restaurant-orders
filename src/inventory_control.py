class InventoryControl:
    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

        self.orders_list = list()

    def add_new_order(self, costumer, order, day):
        self.orders_list.append([costumer, order, day])

    def get_quantities_to_buy(self):
        ingredients_to_buy = {}

        for ingredient in self.minimum_inventory.keys():
            ingredients_to_buy[ingredient] = 0

        for order in self.orders_list:
            dish = order[1]
            for ingredient in self.ingredients[dish]:
                if ingredient not in ingredients_to_buy:
                    ingredients_to_buy[ingredient] = 1
                else:
                    ingredients_to_buy[ingredient] += 1

        return ingredients_to_buy

    def get_available_dishes(self):
        available_dishes = set(self.ingredients.keys())
        for dish, ingredients in self.ingredients.items():
            for ingredient in ingredients:
                minimun = self.minimum_inventory[ingredient]
                if minimun <= self.inventory[ingredient]:
                    available_dishes.remove(dish)
                    break

        return available_dishes
