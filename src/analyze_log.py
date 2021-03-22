import csv
import operator


def analyze_log(path_to_file):
    try:
        if not path_to_file.endswith('.csv'):
            raise FileNotFoundError(
                f"No such file or directory: '{path_to_file}'")
        log = []
        with open(path_to_file, encoding="utf-8") as csv_file:
            restaurant_report = csv.reader(csv_file)

            orders = dict()
            foods = set()
            weekdays = set()

            data = list(restaurant_report)
            for row in data:
                name = row[0]
                food = row[1]
                day = row[2]
                foods.add(food)
                weekdays.add(day)
                if not name in orders:
                    orders[name] = {"weekdays": set(), "foods": {
                        food: 1}, "foodsSet": set()}

                orders[name]["weekdays"].add(day)
                orders[name]["foodsSet"].add(food)

                if not food in orders[name]["foods"]:
                    orders[name]["foods"][food] = 1
                else:
                    orders[name]["foods"][food] += 1

            log.append(max(orders["maria"]["foods"].items(),
                           key=operator.itemgetter(1))[0])
            log.append(orders["arnaldo"]["foods"]["hamburguer"])
            log.append(foods - orders["joao"]["foodsSet"])
            log.append(weekdays - orders["joao"]["weekdays"])

        print(log)
        with open("data/mkt_campaign.txt", "w") as txt_file:
            txt_file.write(f"{log[0]}\n")
            txt_file.write(f"{log[1]}\n")
            txt_file.write(f"{log[2]}\n")
            txt_file.write(f"{log[3]}\n")


    except FileExistsError:
        return f"No such file or directory: '{path_to_file}'"
