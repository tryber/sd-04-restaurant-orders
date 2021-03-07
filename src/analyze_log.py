import csv


def most_ordered_by_person(orders, person):
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


def freq_by_person_product(orders, person, product):
    quantity = 0
    for order in orders[person]:
        if order["product"] == product:
            quantity += 1
    return quantity


def never_ordered_by_person(orders, person, products):
    ordered_products = set()
    for order in orders[person]:
        ordered_products.add(order["product"])
    never_ordered_products = products.difference(ordered_products)
    return never_ordered_products


def never_visited_by_person(orders, person, days):
    visited_days = set()
    for order in orders[person]:
        visited_days.add(order["days"])
    never_visited_days = days.difference(visited_days)
    return never_visited_days


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
            result_file.write(f"{most_ordered_by_person(orders, 'maria')}\n")

            result_file.write(
                f"{freq_by_person_product(orders, 'arnaldo', 'hamburguer')}\n"
            )

            result_file.write(
                f"{never_ordered_by_person(orders, 'joao', products)}\n"
            )

            result_file.write(
                f"{never_visited_by_person(orders, 'joao', days)}"
            )

        result_file.close()
    file.close()
