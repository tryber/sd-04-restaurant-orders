import csv


def read_csv_file(path):
    with open(path, "r") as file:
        read_file = csv.reader(file, delimiter=",", quotechar='"')
        orders_list = list(read_file)
    return orders_list


def orders_by_client(orders_list, client_name):
    orders = {}
    for order in orders_list:
        if order[0] == client_name:
            if order[1] not in orders:
                orders[order[1]] = 1
            else:
                orders[order[1]] += 1
    return orders


def most_ordered_by_client(orders_list, client_name):
    orders = {}
    for order in orders_list:
        if order[0] == client_name:
            if order[1] not in orders:
                orders[order[1]] = 1
            else:
                orders[order[1]] += 1
    return max(orders, key=orders.get)


def order_quantity_by_client(orders_list, client_name, food):
    count = 0
    for order in orders_list:
        if order[0] == client_name:
            if order[1] == food:
                count += 1
    return count


def never_ordered(orders_list, client_name):
    orders = set()
    foods = set()

    # ao invés de acessar o valor pela chave *order[1]* podemos desestruturar:
    for name, food, day in orders_list:
        foods.add(food)
        if client_name == name:
            orders.add(food)
    never_order = foods.difference(orders)
    return never_order


def never_go(orders_list, client_name):
    days = set()
    days_without_client = set()

    for name, food, day in orders_list:
        days.add(day)

        if client_name == name:
            days_without_client.add(day)
    dont_go = days.difference(days_without_client)
    return dont_go


def analyze_log(path_to_file):
    file = read_csv_file(path_to_file)

    answer_1 = f"{most_ordered_by_client(file, 'maria')}\n"
    answer_2 = f"{order_quantity_by_client(file, 'arnaldo', 'hamburguer')}\n"
    answer_3 = f"{never_ordered(file, 'joao')}\n"
    answer_4 = f"{never_go(file, 'joao')}\n"

    with open("data/mkt_campaign.txt", "w") as result:
        result.write(answer_1)
        result.write(answer_2)
        result.write(answer_3)
        result.write(answer_4)
