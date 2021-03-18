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

    def get_available_dishes(self):
        pratos = set()
        ing_0 = set()

        for ing in self.minimum_inventory:
            if ing == 0:
                ing_0.add(ing)
                print(f"ing_0000000000000000000000000000, {ing_0}")

        for prato in self.ingredients:
            for ing in self.ingredients[prato]:
                if ing not in ing_0:
                    pratos.add(prato)
                else:
                    pratos.remove(prato)

        return pratos

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

        ingredientes = self.ingredients[order]
        for ingrediente in ingredientes:
            self.minimum_inventory[ingrediente] -= 1

    def get_quantities_to_buy(self):
        pedido = dict()
        for ing in self.minimum_inventory:
            if ing == 'queijo':
                pedido[ing] = 100 - self.minimum_inventory[ing]
            else:
                pedido[ing] = 50 - self.minimum_inventory[ing]
        return pedido
