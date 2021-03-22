import csv
''' Req 1 '''


def favorite_recipe(orders, name):
    '''Qual o prato mais pedido por 'maria'?'''
    request_favorite = orders[name][0]["product"]
    count_orders = {}

    for order in orders[name]:
        if order["product"] not in count_orders:
            count_orders[order["product"]] = 1
        else:
            count_orders[order["product"]] += 1
        if count_orders[order["product"]] > count_orders[request_favorite]:
            request_favorite = order["product"]

    return request_favorite


def qty_orders(orders, name, item):
    '''Quantas vezes 'arnaldo' pediu 'hamburguer'?'''
    qty = 0

    for order in orders[name]:
        if order["product"] == item:
            qty += 1

    return qty


def not_orders(orders, name, list_of, term):
    '''Quais pratos 'joao' nunca pediu?'''
    client_recipes = set()
    recipes = set(list_of)

    for order in orders[name]:
        client_recipes.add(order[term])

    return recipes.difference(client_recipes)


def analyze_log(path_to_file):
    ''' leitura do log '''
    orders, products, days = reader_csv(path_to_file)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{favorite_recipe(orders, 'maria')}\n")
        file.write(f"{qty_orders(orders, 'arnaldo', 'hamburguer')}\n")
        file.write(f"{not_orders(orders, 'joao', products, 'product')}\n")
        file.write(f"{not_orders(orders, 'joao', days, 'days_of_week')}")


def organized_list(reader_orders):
    products = set()
    days_of_week = set()
    orders = {}

    for name, item, day in reader_orders:
        products.add(item)
        days_of_week.add(day)

        if name not in orders:
            orders[name] = [
                {"product": item, "days_of_week": day}
            ]
        else:
            orders[name].append(
                {"product": item, "days_of_week": day}
            )

    return orders, products, days_of_week


def reader_csv(path):
    with open(path, mode="r") as file:
        reader_orders = csv.reader(file, delimiter=",", quotechar='"')
        orders = organized_list(reader_orders)
    return orders
