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
        ing_0 = set()
        for ing in self.minimum_inventory:
            if self.minimum_inventory[ing] == 0:
                ing_0.add(ing)
        return ing_0

    def get_pratos(self):
        pratos = set()
        for prato in self.ingredients:
            pratos.add(prato)
        return pratos

    def get_available_dishes(self):
        pratos = self.get_pratos()
        list_0 = self.get_ing_list()
        print(f"tesssssste, {pratos}")

        for prato in self.ingredients:
            for ing2 in self.ingredients[prato]:
                if ing2 in list_0 and prato in pratos:
                    print(f"tesssssste, {pratos}")
                    pratos.remove(prato)

        return pratos

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

        ingredientes = self.ingredients[order]
        for ingrediente in ingredientes:
            self.minimum_inventory[ingrediente] -= 1
        # print(f"ooooooooooorder, {order}")
        # if order not in self.get_available_dishes():
        #     return False

    def get_quantities_to_buy(self):
        pedido = dict()
        for ing in self.minimum_inventory:
            if ing == 'queijo':
                pedido[ing] = 100 - self.minimum_inventory[ing]
            else:
                pedido[ing] = 50 - self.minimum_inventory[ing]
        return pedido
