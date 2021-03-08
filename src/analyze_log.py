import csv


def read_the_file(path):
    data = []
    with open(path, encoding="utf-8") as csvfile:
        data_raw = csv.DictReader(csvfile,
        fieldnames = ['name', 'food', 'weekday'])
        for row in data_raw:
            data.append({'name': row['name'], 'food': row['food'], 'weekday': row['weekday']})
        return data


def extract_from_orders(orders, data):
    list_to_extract = set()
    for order in orders:
        list_to_extract.add(order[data])
    return list_to_extract


def count_customer_habits_set (customer_name, habit, habits_list, orders):
    customer = set()
    for order in orders:
        if order['name'] == customer_name:
            customer.add(order[habit])
    return customer


def count_customer_habits (customer_name, habit, habits_list, orders):
    customer = {}
    for one_habit in habits_list:
        customer[one_habit] = 0
    for order in orders:
        if order['name'] == customer_name:
            customer[order[habit]] += 1
    return customer


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    arnaldo_hamburger_ordered = 0
    orders = read_the_file(path_to_file)
    weekday = extract_from_orders(orders, 'weekday')
    foods = extract_from_orders(orders, 'food')
    maria_food = count_customer_habits ("maria", 'food', foods, orders)
    joao_food = count_customer_habits_set ("joao", 'food', foods, orders)
    joao_day = count_customer_habits_set ("joao", 'weekday', weekday, orders)
    for order in orders:
        if order['name'] == 'arnaldo' and order['food'] == 'hamburguer':
            arnaldo_hamburger_ordered += 1
    max_ordered = max(maria_food, key=maria_food .get)
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{max_ordered}\n")
        file.write(f"{arnaldo_hamburger_ordered}\n")
        file.write(f"{foods.difference(joao_food)}\n")
        file.write(f"{weekday.difference(joao_day)}")
