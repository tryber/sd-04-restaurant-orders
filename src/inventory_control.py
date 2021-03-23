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

        self.buy_list = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

        self.orders = list()

    def add_new_order(self, costumer, order, day):
        ingredients = self.ingredients[order]
        for ingredient in ingredients:
            if self.minimum_inventory[ingredient] == 0:
                return False

            self.minimum_inventory[ingredient] -= 1

            if ingredient not in self.buy_list:
                self.buy_list[ingredient] = 1
            else:
                self.buy_list[ingredient] += 1

        self.orders.append([costumer, order, day])

    def get_quantities_to_buy(self):
        return self.buy_list

    def get_available_dishes(self):
        avaliable_foods = set()
        for dishe, ingredients in self.ingredients.items():
            avaliable = True
            for item in ingredients:
                print(self.minimum_inventory[item])
                if self.minimum_inventory[item] == 0:
                    avaliable = False

            if avaliable:
                avaliable_foods.add(dishe)

        return avaliable_foods
