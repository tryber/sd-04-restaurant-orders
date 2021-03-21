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
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        if order not in self.get_available_dishes():
            return False

        for ingredient in self.ingredients[order]:
            self.inventory[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        pratos = set(self.ingredients.keys())
        for prato, ingredients in self.ingredients.items():
            for ingredient in ingredients:
                min = self.minimum_inventory[ingredient]
                if min <= self.inventory[ingredient]:
                    pratos.remove(prato)
                    return pratos
        return pratos
