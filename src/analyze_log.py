import csv
from collections import defaultdict, Counter


class Order:
    def __init__(self):
        self.dishes = Counter()
        self.weekdays = Counter()

    def add(self, dish, weekday):
        self.dishes[dish] += 1
        self.weekdays[weekday] += 1


class TxtWriter:
    def __init__(self, lines):
        self.lines = [TxtWriter.add_sufix(line) for line in lines]

    @staticmethod
    def add_sufix(txt):
        if not isinstance(txt, str):
            txt = str(txt)
        return txt + ";\n"

    def save_file(self, path):
        with open(path, "w", encoding="utf-8") as file:
            file.writelines(self.lines)


def extract_restaurant_info(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: {path_to_file}")

    with open(path_to_file, encoding="utf-8") as file:
        data = list(csv.reader(file))

    orders = defaultdict(Order)
    info = defaultdict(set)

    for name, dish, weekday in data:
        orders[name].add(dish, weekday)
        info["all_dishes"].add(dish)
        info["all_weekdays"].add(weekday)

    return [orders, info]


def analyze_log(path_to_file):
    orders, info = extract_restaurant_info(path_to_file)

    joao_dishes = set(orders["joao"].dishes.keys())
    joao_weekdays = set(orders["joao"].weekdays.keys())

    writer = TxtWriter([
            orders['maria'].dishes.most_common(1)[0][0],
            orders["arnaldo"].dishes["hamburguer"],
            info["all_dishes"] - joao_dishes,
            info["all_weekdays"] - joao_weekdays,
    ])
    writer.save_file('data/mkt_campaign.txt')



analyze_log("./data/orders_1.csv")
