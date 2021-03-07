import csv
from collections import Counter


def get_answers(orders_list):
    all_orders = set()
    all_days = set()

    orders_maria = list()
    orders_arnaldo = list()
    orders_joao = set()
    days_joao = set()

    for name, order, day in orders_list:
        all_orders.add(order)
        all_days.add(day)
        if name == "maria":
            orders_maria.append(order)
        if name == "arnaldo":
            orders_arnaldo.append(order)
        if name == "joao":
            orders_joao.add(order)
            days_joao.add(day)

    answers_list = list()
    answers_list.append(list(Counter(orders_maria))[0])
    answers_list.append(dict(Counter(orders_arnaldo))["hamburguer"])
    answers_list.append(all_orders - orders_joao)
    answers_list.append(all_days - days_joao)

    return answers_list


def analyze_log(path_to_file):
    try:
        orders_list = list()
        with open(path_to_file) as csv_file:
            reader = csv.reader(csv_file)
            for costumer, order, day in reader:
                orders_list.append([costumer, order, day])
            csv_file.close()

        answers = get_answers(orders_list)

    except (FileNotFoundError):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    else:
        with open("data/mkt_campaign.txt", "w") as txt_file:
            for answer in answers:
                txt_file.write(str(answer) + "\n")
        txt_file.close()
