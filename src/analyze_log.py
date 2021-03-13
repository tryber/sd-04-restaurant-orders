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
