class InventoryControl:
    def __init__(self):
        self.orders = []
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
        self.inventory = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        if order not in self.get_available_dishes():
            return False

        for ing in self.ingredients[order]:
            self.inventory[ing] += 1

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        available_dishes = list(self.ingredients.keys())
        for dish, ings in self.ingredients.items():
            for ing in ings:
                min_ing = self.minimum_inventory[ing]
                if min_ing <= self.inventory[ing]:
                    available_dishes.remove(dish)
                    break

        return set(available_dishes)