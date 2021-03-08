import csv


def read_the_file(path):
    data = []
    with open(path, encoding="utf-8") as csvfile:
        data_raw = csv.DictReader(csvfile,
                                  fieldnames=['name', 'food', 'weekday'])
        for row in data_raw:
            data.append([row['name'], row['food'], row['weekday']])
        return data


def file_to_dic(orders):
    data = [] 
    for order in orders:
        data.append({'name': order[0],
                    'food': order[1], 'weekday': order[2]})
    return data


def extract_from_orders(orders, data):
    list_to_extract = set()
    for order in orders:
        list_to_extract.add(order[data])
    return list_to_extract


def count_customer_habits_set(customer_name, habit, file_readd):
    orders = file_to_dic(file_readd)
    habits_list = extract_from_orders(orders, habit)
    customer = set()
    for order in orders:
        if order['name'] == customer_name:
            customer.add(order[habit])
    return habits_list.difference(customer)


def count_customer_habits(customer_name, habit, file_readd):
    orders = file_to_dic(file_readd)
    habits_list = extract_from_orders(orders, habit)
    customer = {}
    for one_habit in habits_list:
        customer[one_habit] = 0
    for order in orders:
        if order['name'] == customer_name:
            customer[order[habit]] += 1
    max_ordered = max(customer, key=customer .get)
    return max_ordered


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    arnaldo_hamburger_ordered = 0
    file_readd = read_the_file(path_to_file)
    orders = file_to_dic(file_readd)
    weekday = extract_from_orders(orders, 'weekday')
    foods = extract_from_orders(orders, 'food')
    max_ordered = count_customer_habits("maria", 'food', file_readd)
    joao_food = count_customer_habits_set("joao", 'food', file_readd)
    joao_day = count_customer_habits_set("joao", 'weekday', file_readd)
    for order in orders:
        if order['name'] == 'arnaldo' and order['food'] == 'hamburguer':
            arnaldo_hamburger_ordered += 1
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{max_ordered}\n")
        file.write(f"{arnaldo_hamburger_ordered}\n")
        file.write(f"{joao_food}\n")
        file.write(f"{joao_day}")
        # file.write(f"{foods.difference(joao_food)}\n")
        # file.write(f"{weekday.difference(joao_day)}")
