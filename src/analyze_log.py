import csv
from collections import defaultdict


def analyze_log(path_to_file):
    with open(path_to_file, encoding='utf-8') as file:
        data = list(csv.reader(file))
    all_dishes = set()
    all_weekdays = set()
    orders = defaultdict(lambda: {'dishes': defaultdict(int), 'weekdays': defaultdict(int)})

    maria_dish = None

    for name, dish, weekday in data:
        this_order = orders[name]
        dishes = this_order['dishes']
        dishes[dish] += 1
        this_order['weekdays'][weekday] += 1
        all_dishes.add(dish)
        all_weekdays.add(weekday)
        if (name == 'maria' and dishes[dish] > dishes[maria_dish] or not maria_dish):
            maria_dish = dish

    lines = []
    def append_line(txt):
        if not isinstance(txt, str):
            txt = str(txt)
        lines.append(txt + ';\n')
    append_line(maria_dish)
    append_line(orders['arnaldo']['dishes']['hamburguer'])

    joao_dishes = set(orders['joao']['dishes'].keys())
    append_line(all_dishes - joao_dishes)
    joao_weekdays = set(orders['joao']['weekdays'].keys())
    append_line(all_weekdays - joao_weekdays)

    with open('data/mkt_campaign.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)

analyze_log('./data/orders_1.csv')
