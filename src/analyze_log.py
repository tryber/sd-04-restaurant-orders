import csv


def most_ordered_by_customer(orders_list, customer_name):
    orders = {}
    for order in orders_list:
        if order[0] == customer_name:
            if order[1] not in orders:
                orders[order[1]] = 1
            else:
                orders[order[1]] += 1
    return max(orders, key=orders.get)


def order_qty_by_customer(orders_list, customer_name, food):
    count = 0
    for order in orders_list:
        if order[0] == customer_name:
            if order[1] == food:
                count += 1
    return count


def never_ordered(orders_list, customer_name):
    orders = set()
    foods = set()

    for name, food, _ in orders_list:
        foods.add(food)
        if customer_name == name:
            orders.add(food)
    never_order = foods.difference(orders)
    return never_order


def never_visited(orders_list, customer_name):
    days = set()
    days_without_client = set()

    for name, _, day in orders_list:
        days.add(day)

        if customer_name == name:
            days_without_client.add(day)
    dont_go = days.difference(days_without_client)
    return dont_go


def analyze_log(path_to_file):
    with open(path_to_file, "r") as csv_file:
        read_file = csv.reader(csv_file, delimiter=",", quotechar='"')
        orders_list = list(read_file)

    with open("data/mkt_campaign.txt", "w") as result:
        result.write(f"{most_ordered_by_customer(orders_list, 'maria')}\n")
        result.write(
            f"{order_qty_by_customer(orders_list, 'arnaldo', 'hamburguer')}\n"
        )
        result.write(f"{never_ordered(orders_list, 'joao')}\n")
        result.write(f"{never_visited(orders_list, 'joao')}\n")
