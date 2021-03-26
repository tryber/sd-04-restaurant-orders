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

        self.inventory = {
            'carne': 0,
            'pao': 0,
            'frango': 0,
            'molho': 0,
            'massa': 0,
            'queijo': 0,
            'presunto': 0,
        }

    def add_new_order(self, costumer, order, day):
        for item in self.ingredients[order]:
            if self.minimum_inventory[item] == 0:
                return False
            self.minimum_inventory[item] -= 1
            if item in self.inventory:
                self.inventory[item] += 1
            else:
                self.inventory[item] = 1

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        dishes = set(self.ingredients.keys())
        for dish, ingredients in self.ingredients.items():
            for ingredient in ingredients:
                if self.minimum_inventory[ingredient] == 0:
                    dishes.remove(dish)
                    break
        return dishes
