import csv


def most_ordered_by_client(orders, name):
    count =  {}
    request_favorite = orders[name][0]["product"]

    for order in orders[name]:
        if order["product"] not in count:
            count[order["product"]] = 1
        else:
            count[order["product"]] += 1
        if count[order["product"]] > count[request_favorite]:
            request_favorite = order["product"]

    return request_favorite


def times_ordered(orders, name, item):
    times = 0

    for order in orders[name]:
        if order["product"] == item:
            times += 1

    return times


def not_ordered(orders, name, list_of, term):
    recipes = set(list_of)
    client_recipes = set()

    for order in orders[name]:
        client_recipes.add(order[term])

    return recipes.difference(client_recipes)


def analyze_log(path_to_file):
    orders, products, days = reader_csv(path_to_file)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{most_ordered_by_client(orders, 'maria')}\n")
        file.write(f"{times_ordered(orders, 'arnaldo', 'hamburguer')}\n")
        file.write(f"{not_ordered(orders, 'joao', products, 'product')}\n")
        file.write(f"{not_ordered(orders, 'joao', days, 'days_of_week')}")


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
