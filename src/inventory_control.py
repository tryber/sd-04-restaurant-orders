class InventoryControl:
    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.orders_list = list()

    def add_new_order(self, costumer, order, day):
        return self.orders_list.append([costumer, order, day])

    def get_quantities_to_buy(self):
        ingredients_to_buy = {}
        for ingredient in self.minimum_inventory.keys():
            ingredients_to_buy[ingredient] = 0
        for costumer, order, day in self.orders_list:
            for ingredient in self.ingredients[order]:
                if ingredient not in ingredients_to_buy:
                    ingredients_to_buy[ingredient] = 1
                else:
                    ingredients_to_buy[ingredient] += 1
        return ingredients_to_buy

    def get_ingredients_not_available(self):
        not_available_ingredients = set()
        for ingredient in self.minimum_inventory:
            not_available_ingredients.add(ingredient)
        return not_available_ingredients
    
    def get_available_dishes(self):
        return set(self.ingredients.keys())
