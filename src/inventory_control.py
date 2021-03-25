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

        self.ingredients_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        for item in self.ingredients[order]:
            if self.minimum_inventory[item] == 0:
                return False
            self.minimum_inventory[item] -= 1
            if item in self.ingredients_to_buy:
                self.ingredients_to_buy[item] += 1
            else:
                self.ingredients_to_buy[item] = 1

    def get_quantities_to_buy(self):
        return self.ingredients_to_buy

    def get_available_dishes(self):
        dishes = set(self.ingredients.keys())
        for dish, ingredients in self.ingredients.items():
            for item in ingredients:
                if self.minimum_inventory[item] == 0:
                    dishes.remove(dish)
        return dishes
