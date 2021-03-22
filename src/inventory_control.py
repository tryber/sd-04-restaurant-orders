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
    def prato(self):
        prato = set()
        for ref in self.ingredients:
            prato.add(ref)
        return prato

    def ingre_disp(self):
        ingre_disp = set()
        for ingre in self.minimum_inventory:
            if self.minimum_inventory[ingre] > 0:
                ingre_disp.add(ingre)
        return ingre_disp

    def get_available_dishes(self):
        pratos = self.prato()
        ingre_disp = self.ingre_disp()
        for prato in self.ingredients:
            for ingre in self.ingredients[prato]:
                if not ingre in ingre_disp and prato in pratos:
                    pratos.remove(prato)
        return pratos

    def add_new_order(self, costumer, order, day):
        self.orders_list.append([costumer, order, day])
        array = []
        control = self.ingredients[order]
        for ingre in control:
            array.append(ingre)
        counter_ingre = Counter(array)
        for ing in counter_ingre:
            if self.minimum_inventory[ing] > 0:
                self.minimum_inventory[ing] = self.minimum_inventory[ing] - \
                    counter_ingre[ing]
            else:
                return False
        self.get_available_dishes()
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
