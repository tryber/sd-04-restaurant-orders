import csv


def best_seller_by_client(client, dict):
    count = {}
    client_list = dict[client]
    client_dish_and_day = client_list[0]
    most_frequent = client_dish_and_day[0]

    for dish, day in client_list:
        if dish not in count:
            count[dish] = 1
        else:
            count[dish] += 1
        if count[dish] > count[most_frequent]:
            most_frequent = dish
    return most_frequent


def favorite_dish_by_client(client, selected_dish, dict):
    count = {}
    client_list = dict[client]
    for dish, day in client_list:
        if dish not in count:
            count[dish] = 1
        else:
            count[dish] += 1
    return count[selected_dish]


def get_total_dish(dict):
    dishes = set()
    for client, orders in dict.items():
        for tuples in orders:
            dishes.add(tuples[0])
    return dishes


def get_total_days(dict):
    days = set()
    for client, orders in dict.items():
        for tuples in orders:
            days.add(tuples[1])
    return days


def never_ordered(client, dishes, dict):
    client_list = dict[client]
    client_dishes = set()
    for orders in client_list:
        client_dishes.add(orders[0])
    return dishes.difference(client_dishes)


def never_be_in_day(client, days, dict):
    client_list = dict[client]
    client_days = set()
    for orders in client_list:
        client_days.add(orders[1])
    return days.difference(client_days)


def write_lines_in_txt(filepath, lines):
    with open(filepath, "w") as file:
        for line in lines:
            file.writelines(f"{line}\n")


def analyze_log(path_to_file):
    data = {}

    with open(path_to_file, "r") as csv_file:
        csv_dict = csv.reader(csv_file, delimiter=",")
        for name, dish, day in csv_dict:
            if name not in data:
                data[name] = [(dish, day)]
            else:
                data[name].append((dish, day))

    dishes = get_total_dish(data)
    days = get_total_days(data)
    report = []

    report.append(best_seller_by_client("maria", data))
    report.append(favorite_dish_by_client("arnaldo", "hamburguer", data))
    report.append(never_ordered("joao", dishes, data))
    report.append(never_be_in_day("joao", days, data))

    write_lines_in_txt("data/mkt_campaign.txt", report)
