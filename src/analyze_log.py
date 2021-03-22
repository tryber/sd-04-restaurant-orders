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
    for row in data:
        foods.add(row[1])
        weekdays.add(row[2])

        if row[0] not in orders:
            orders[row[0]] = {"weekdays": set(), "foods": {
                row[1]: 1}, "foodsSet": set()}

        orders[row[0]]["weekdays"].add(row[2])
        orders[row[0]]["foodsSet"].add(row[1])

        if row[1] not in orders[row[0]]["foods"]:
            orders[row[0]]["foods"][row[1]] = 1
        else:
            orders[row[0]]["foods"][row[1]] += 1

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
