from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders_list = []

    def __len__(self):
        return len(self.orders_list)

    def add_new_order(self, costumer, order, day):
        self.orders_list.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        lista = []
        for order in self.orders_list:
            if order[0] == costumer:
                lista.append(order[1])
        most = Counter(lista)  # cria um contador
        biggest_value = max(most.values())
        # retorna o VALOR do maior contador
        biggest_keys = [key for key, value in most.items() if value ==
                        biggest_value]
        # faço um for in trazendo chave e valor e
        # retorno o que tem o mesmo valor maximo
        return biggest_keys[0]

    def get_order_frequency_per_costumer(self, costumer, order):
        count = 0
        for orders in self.orders_list:
            if orders[0] == costumer and orders[1] == order:
                count += 1
        return count

    def get_never_ordered_per_costumer(self, costumer):
        set_costumer = set()
        set_resto = set()
        for order in self.orders_list:
            if order[0] == costumer:
                set_costumer.add(order[1])
            else:
                set_resto.add(order[1])
        return set_resto.difference(set_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        set_costumer = set()
        set_resto = set()
        for order in self.orders_list:
            if order[0] == costumer:
                set_costumer.add(order[2])
            else:
                set_resto.add(order[2])
        return set_resto.difference(set_costumer)

    def get_busiest_day(self):
        lista = []
        for order in self.orders_list:
            lista.append(order[2])
        most = Counter(lista)  # cria um contador
        biggest_value = max(most.values())
        # retorna o VALOR do maior contador
        biggest_keys = [key for key, value in most.items() if value ==
                        biggest_value]
        # faço um for in trazendo chave e valor e
        # retorno o que tem o mesmo valor maximo
        return biggest_keys[0]

    def get_least_busy_day(self):
        lista = []
        for order in self.orders_list:
            lista.append(order[2])
        most = Counter(lista)  # cria um contador
        biggest_value = min(most.values())
        # retorna o VALOR do menor contador
        biggest_keys = [key for key, value in most.items() if value ==
                        biggest_value]
        # faço um for in trazendo chave e valor e
        # retorno o que tem o mesmo valor maximo
        return biggest_keys[0]
