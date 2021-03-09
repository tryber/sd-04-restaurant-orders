import csv


def organized_list(read_orders):
    order_list = {}
    products = set()
    days_of_week = set()

    for client, item, day in read_orders:
        products.add(item)
        days_of_week.add(day)
        if client not in order_list:
            order_list[client] = [
                {"product": item, "days_of_week": day}
            ]
        else:
            order_list[client].append(
                {"product": item, "days_of_week": day}
            )

    return order_list, products, days_of_week


def read_csv(path):
    with open(path, mode="r") as file:
        reader_csv = csv.reader(file, delimiter=",", quotechar='"')
        orders_list = organized_list(reader_csv)
    return orders_list


def most_request(order_list, client):
    requested = order_list[client][0]["product"]
    count = {}
    for order in order_list[client]:
        if order["product"] not in count:
            count[order["product"]] = 1
        else:
            count[order["product"]] += 1
        if count[order["product"]] > count[requested]:
            requested = order["product"]

    return requested


def count_asked(order_list, client, food):
    count = 0
    for order in order_list[client]:
        if order["product"] == food:
            count += 1

    return count


def never_ordered(order_list, client, list_of, term):
    dishes = set()
    client_orders = set(list_of)
    for order in order_list[client]:
        dishes.add(order[term])

    return (client_orders.difference(dishes))


def analyze_log(path_to_file):
    order_list, products, days = read_csv(path_to_file)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{most_request(order_list, 'maria')}\n")
        file.write(f"{count_asked(order_list, 'arnaldo', 'hamburguer')}\n")
        file.write(
            f"{never_ordered(order_list, 'joao', products, 'product')}\n")
        file.write(
            f"{never_ordered(order_list, 'joao', days, 'days_of_week')}")
