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

    def get_quantities_to_buy(self):

        for _, order, _ in self.orders:
            if order == "hamburguer":
                self.inventory["pao"] += 1
                self.inventory["carne"] += 1
                self.inventory["queijo"] += 1

            if order == "pizza":
                self.inventory["massa"] += 1
                self.inventory["molho"] += 1
                self.inventory["queijo"] += 1

            if order == "misto-quente":
                self.inventory["pao"] += 1
                self.inventory["presunto"] += 1
                self.inventory["queijo"] += 1
            if order == "coxinha":
                self.inventory["massa"] += 1
                self.inventory["frango"] += 1
        return self.inventory
