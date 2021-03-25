import csv


def most_ordered(orders, person):
    quantity = {}
    most_ordered = orders[person][0]["product"]
    for order in orders[person]:
        if order["product"] not in quantity:
            quantity[order["product"]] = 1
        else:
            quantity[order["product"]] += 1
        if quantity[order["product"]] > quantity[most_ordered]:
            most_ordered = order["product"]

    return most_ordered


def freq_ordered(orders, person, product):
    quantity = 0
    for order in orders[person]:
        if order["product"] == product:
            quantity += 1
    return quantity


def never_set(orders, person, items, index):
    superset = set()
    for order in orders[person]:
        superset.add(order[index])
    never_set = items.difference(superset)
    return never_set


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as file:
        orders_reader = csv.reader(file, delimiter=",")

        orders = {}
        products = set()
        days = set()

        for person, product, day in orders_reader:
            products.add(product)
            days.add(day)
            if person in orders:
                orders[person].append({"product": product, "days": day})
            else:
                orders[person] = [{"product": product, "days": day}]

        with open("data/mkt_campaign.txt", mode="w") as result_file:
            result_file.write(f"{most_ordered(orders, 'maria')}\n")

            result_file.write(
                f"{freq_ordered(orders, 'arnaldo', 'hamburguer')}\n"
            )

            result_file.write(
                f"{never_set(orders, 'joao', products, 'product')}\n"
            )

            result_file.write(f"{never_set(orders, 'joao', days, 'days')}")

        result_file.close()
    file.close()
