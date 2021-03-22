from collections import Counter


class InventoryControl:
    def __init__(self):
        self.orders_list = []

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

    def add_new_order(self, costumer, order, day):
        self.orders_list.append([costumer, order, day])
        array = []
        control = self.ingredients[order]
        for ingre in control:
            array.append(ingre)
        counter_ingre = Counter(array)
        for ingre in counter_ingre:
            self.minimum_inventory[ingre] = self.minimum_inventory[ingre] - \
                counter_ingre[ingre]
        return True

    def get_quantities_to_buy(self):
        compras = dict()
        for ingre in self.minimum_inventory:
            if ingre == 'queijo':
                compras[ingre] = 100 - \
                    self.minimum_inventory[ingre]
            else:
                compras[ingre] = 50 - \
                    self.minimum_inventory[ingre]
        return compras
