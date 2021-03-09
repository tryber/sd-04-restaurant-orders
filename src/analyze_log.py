import operator
import csv


def ordered_dish_per_costumer(data, person):
    costumer_meals = {}

    for name, meal, day in data:
        if person == name:
            if meal not in costumer_meals:
                costumer_meals[meal] = 0
            else:
                costumer_meals[meal] += 1
    max_ordered = max(costumer_meals.items(), key=operator.itemgetter(1))[0]
    return max_ordered


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    with open(path_to_file, "r") as file:
        content = csv.reader(file, delimiter=",")
        return data = list(content)

    with open("data/mkt_campaign.txt", "w") as analyze_file:
        analyze_file.write(f"{ordered_dish_per_costumer(data, 'maria')}\n")
