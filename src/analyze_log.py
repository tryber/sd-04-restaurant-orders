import csv
from collections import defaultdict


def get_working_days(reader):
    working_days = set()
    for order in reader:
        working_days.add(order[2])
    return working_days


def get_dishes(reader):
    dishes = set()
    for order in reader:
        dishes.add(order[1])
    return dishes


def get_most_ordered_dish(reader, customer_name):
    ordered_dishes = defaultdict(int)
    for order in reader:
        if order[0] == customer_name:
            ordered_dishes[order[1]] += 1
    ordered_dishes_result = dict(ordered_dishes)
    return max(ordered_dishes_result, key=ordered_dishes_result.get)


def get_dish_count_by_person(reader, customer_name, dish):
    dish_count = 0
    for order in reader:
        if order[0] == customer_name and order[1] == dish:
            dish_count += 1
    return dish_count


def get_never_ordered_by_person(reader, customer_name):
    ordered = set()
    dishes = get_dishes(reader)
    for order in reader:
        if order[0] == customer_name:
            ordered.add(order[1])
    return dishes.difference(ordered)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise ValueError("Invalid file extension")
    with open(path_to_file) as file:
        orders_reader = csv.reader(file, delimiter=",")
        test = get_never_ordered_by_person(orders_reader, "joao")
        # test2 = get_dishes(orders_reader)
        # dishes = set()
        # marias_dishes_ddict = defaultdict(int)
        # arnaldos_hamburguer_count = 0
        # joaos_ordered = set()
        # joao_went = set()
        # for order in orders_reader:
        #     # week_days.add(order[2])
        #     dishes.add(order[1])
        #     if order[0] == "maria":
        #         marias_dishes_ddict[order[1]] += 1
        #     if order[0] == "arnaldo" and order[1] == "hamburguer":
        #         arnaldos_hamburguer_count += 1
        #     if order[0] == "joao":
        #         joaos_ordered.add(order[1])
        #         joao_went.add(order[2])

        # marias_dishes = dict(marias_dishes_ddict)
        # marias_most_ordered = max(marias_dishes, key=marias_dishes.get)
        # joaos_not_ordered = dishes.difference(joaos_ordered)
        # joao_didnt_went = week_days.difference(joao_went)
        print(test)


analyze_log("data/orders_1.csv")
