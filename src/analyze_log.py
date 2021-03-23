import csv
import operator


def create_txt_file(log):
    with open("data/mkt_campaign.txt", "w") as txt_file:
        txt_file.write(f"{log[0]}\n")
        txt_file.write(f"{log[1]}\n")
        txt_file.write(f"{log[2]}\n")
        txt_file.write(f"{log[3]}\n")


def create_log_report(report):
    orders = dict()
    foods = set()
    weekdays = set()
    data = list(report)
    restaurant_log = []
    for costumer, order, day in data:
        foods.add(order)
        weekdays.add(day)

        if costumer not in orders:
            orders[costumer] = {"weekdays": set(), "foods": {
                order: 1}, "foodsSet": set()}

        orders[costumer]["weekdays"].add(day)
        orders[costumer]["foodsSet"].add(order)

        if order not in orders[costumer]["foods"]:
            orders[costumer]["foods"][order] = 1
        else:
            orders[costumer]["foods"][order] += 1

    restaurant_log.append(max(orders["maria"]["foods"].items(),
                              key=operator.itemgetter(1))[0])
    restaurant_log.append(orders["arnaldo"]["foods"]["hamburguer"])
    restaurant_log.append(foods - orders["joao"]["foodsSet"])
    restaurant_log.append(weekdays - orders["joao"]["weekdays"])

    return restaurant_log


def analyze_log(path_to_file):
    try:
        if not path_to_file.endswith('.csv'):
            raise FileNotFoundError(
                f"No such file or directory: '{path_to_file}'")
        with open(path_to_file, encoding="utf-8") as csv_file:
            restaurant_report = csv.reader(csv_file)
            log = create_log_report(restaurant_report)
            create_txt_file(log)

    except FileExistsError:
        return f"No such file or directory: '{path_to_file}'"
