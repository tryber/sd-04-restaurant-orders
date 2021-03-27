class InventoryControl:
    def __init__(self):
        self.orders = []
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

    def get_ing_list(self):
        ing_1 = set()
        for ing in self.minimum_inventory:
            if self.minimum_inventory[ing] == 0:
                ing_1.add(ing)
        return ing_1

    def get_dishes(self):
        dishes = set()
        for prato in self.ingredients:
            dishes.add(prato)
        return dishes

    def get_available_dishes(self):
        pratos = self.get_dishes()
        list_1 = self.get_ing_list()
        for prato in self.ingredients:
            for ing2 in self.ingredients[prato]:
                if ing2 in list_1 and prato in pratos:
                    pratos.remove(prato)
        return pratos

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

        ingredientes = self.ingredients[order]
        for ingrediente in ingredientes:
            if self.minimum_inventory[ingrediente] > 0:
                self.minimum_inventory[ingrediente] -= 1
            else:
                return False
        lista = self.get_available_dishes()
        print(f"ooooooooooorder, {order}")
        print(f"ingredientes, {self.minimum_inventory}")
        print(f"lista, {lista}")
        if order not in lista:
            return False

    def get_quantities_to_buy(self):
        pedido = dict()
        for ing in self.minimum_inventory:
            if ing == 'queijo':
                pedido[ing] = 100 - self.minimum_inventory[ing]
            else:
                pedido[ing] = 50 - self.minimum_inventory[ing]
        return pedido
