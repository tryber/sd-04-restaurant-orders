''' Req 1 '''
'''Qual o prato mais pedido por 'maria'?'''


def favorite_recipe(orders, costumer):
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


'''Quantas vezes 'arnaldo' pediu 'hamburguer'?'''


def qty_orders(orders, costumer, recipe):
    qty = 0

    for name, order, day in orders:
        if name == costumer and order == recipe:
            qty += 1

    return qty


'''Quais pratos 'joao' nunca pediu?'''


def not_orders(orders, costumer):
    recipes = set()
    client_recipes = set()

    for name, order, day in orders:
        recipes.add(order)

        if name == costumer:
            client_recipes.add(order)

    return recipes.difference(client_recipes)
