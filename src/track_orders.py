class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        pedidos = []
        maior = set()
        for line in self.orders:
            if line[0] == costumer:
                pedidos.append(line[1])
        for pedido in pedidos:
            maior.add((pedidos.count(pedido), pedido))
            maior2 = dict(maior)
        return maior2[max(maior2)]

    def get_order_frequency_per_costumer(self, costumer, order):
        pedidos = []
        for line in self.orders:
            if line[0] == costumer:
                pedidos.append(line[1])
        return pedidos.count(order)

    def get_never_ordered_per_costumer(self, costumer):
        pedidos = set()
        pedidos_cliente = set()
        for line in self.orders:
            if line[0] == costumer:
                pedidos_cliente.add(line[1])
            else:
                pedidos.add(line[1])
        return pedidos - pedidos_cliente

    def get_days_never_visited_per_costumer(self, costumer):
        dias = set()
        dias_cliente = set()
        for line in self.orders:
            if line[0] == costumer:
                dias_cliente.add(line[2])
            else:
                dias.add(line[2])
        return dias - dias_cliente

    def get_busiest_day(self):
        pedidos = []
        maior = set()
        for line in self.orders:
            pedidos.append(line[2])
        for pedido in pedidos:
            maior.add((pedidos.count(pedido), pedido))
            maior2 = dict(maior)
        # print(f"pedidos, {pedidos}")
        # print(f"maior, {maior}")
        return maior2[max(maior2)]

    def get_least_busy_day(self):
        pedidos = []
        maior = set()
        for line in self.orders:
            pedidos.append(line[2])
        for pedido in pedidos:
            maior.add((pedidos.count(pedido), pedido))
            maior2 = dict(maior)
        # print(f"pedidos, {pedidos}")
        # print(f"maior, {maior}")
        return maior2[min(maior2)]
