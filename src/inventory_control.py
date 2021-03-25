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

        self._data = list()

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
        u_ingredients = self.ingredients_used

        if order not in self.get_available_dishes():
            return False

        for item in self.ingredients[order]:
            self.minimum_inventory[item] -= 1
            u_ingredients[item] += 1

        self._data.append([costumer, order, day])

    def get_quantities_to_buy(self):
        return self.ingredients_used

    def get_available_dishes(self):
        stock = set()
        for food, ingredients in self.ingredients.items():
            available = True
            for ing in ingredients:
                if self.minimum_inventory[ing] == 0:
                    available = False

            if (available):
                stock.add(food)

        return stock
