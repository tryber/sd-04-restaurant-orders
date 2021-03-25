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

        # self._data = list()
        self.ingredients_used = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, costumer, order, day):
        ingredients = self.ingredients_used
        for item in self.ingredients[order]:
            self.minimum_inventory[item] -= 1
            ingredients[item] += 1
        # print(ingredients)
        # print(self.minimum_inventory)
        # self._data.append([costumer, order, day])

    def get_quantities_to_buy(self):
        return self.ingredients_used
