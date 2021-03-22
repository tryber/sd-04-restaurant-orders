class InventoryControl:
    def __init__(self):
        self.ingredients = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            "misto-quente": ["pao", "queijo", "presunto"],
            "coxinha": ["massa", "frango"],
        }

        self.minimum_inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

        self.quantities_inventory = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

        self.all_dishes = set(
            [
                "hamburguer",
                "pizza",
                "misto-quente",
                "coxinha",
            ]
        )

    def remover_pedido(self, ingredient):
        for dish in self.ingredients:
            actual_ingredients = set(self.ingredients[dish])
            if ingredient in actual_ingredients:
                self.all_dishes.discard(dish)

    def adicionar_pedido(self, costumer, order, day):
        pass
        elements = self.ingredients[order]
        for ingredient in elements:
            if (
                self.quantities_inventory[ingredient] + 1
                < self.minimum_inventory[ingredient]
            ):
                self.quantities_inventory[ingredient] += 1
            elif (
                self.quantities_inventory[ingredient]
                < self.minimum_inventory[ingredient]
            ):
                self.quantities_inventory[ingredient] += 1
                self.remover_pedido(ingredient)
            else:
                return False

    def get_quantities_to_buy(self):
        pass
        return self.quantities_inventory

    def get_available_dishes(self):
        return self.all_dishes
