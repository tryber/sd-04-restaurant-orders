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

        self.inventory = self.minimum_inventory.copy()

    def add_new_order(self, costumer, order, day):
        for ingredient in self.ingredients[order]:
            if self.inventory[ingredient] == 0:
                return False

            self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        return dict([
            (ingredient, self.minimum_inventory[ingredient]
                - self.inventory[ingredient])

            for ingredient in self.minimum_inventory
        ])

    def get_available_dishes(self):
        return {
            dish for dish in self.ingredients if self.is_dish_avaible(dish)
        }

    def is_dish_avaible(self, dish):
        for ingredient in self.ingredients[dish]:
            if self.inventory[ingredient] == 0:
                return False

        return True
