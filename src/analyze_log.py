import csv
''' Req 1 '''


def favorite_recipe(orders, costumer):
    '''Qual o prato mais pedido por 'maria'?'''
    request_favorite = ""
    list_orders = {}

    for name, order, day in orders:
        if name == costumer:
            if order not in list_orders:
                list_orders[order] = 1
            else:
                list_orders[order] += 1

            if (
                request_favorite not in list_orders
                or list_orders[order] > list_orders[request_favorite]
            ):
                request_favorite = order

    return request_favorite


def qty_orders(orders, costumer, recipe):
    '''Quantas vezes 'arnaldo' pediu 'hamburguer'?'''
    qty = 0

    for name, order, day in orders:
        if name == costumer and order == recipe:
            qty += 1

    return qty


def not_orders(orders, costumer):
    '''Quais pratos 'joao' nunca pediu?'''
    recipes = set()
    client_recipes = set()

    for name, order, day in orders:
        recipes.add(order)

        if name == costumer:
            client_recipes.add(order)

    return recipes.difference(client_recipes)


def client_days_off(orders, costumer):
    ''' Quais dias 'joao' nunca foi na lanchonete?'''
    days = set()
    client_visited = set()

    for name, order, day in orders:
        days.add(day)

        if name == costumer:
            client_visited.add(day)

    return days.difference(client_visited)


def analyze_log(path_to_file):
    ''' leitura do log '''
    with open(path_to_file, "r") as teste:
        leitura = csv.reader(teste, delimiter=",")
        info = [*leitura]

        favorite_recipe_save = favorite_recipe(info, "maria")
        qty_orders_save = qty_orders(info, "arnaldo", "hamburguer")
        not_orders_save = not_orders(info, "joao")
        client_days_off_save = client_days_off(info, "joao")

        with open("data/mkt_campaign.txt", "w") as file:
            print(
                favorite_recipe_save,
                qty_orders_save,
                not_orders_save,
                client_days_off_save,
                sep="\n",
                file=file,
            )
