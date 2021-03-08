import csv
import operator

def analyze_log(path_to_file):
    food = []
    weekday = []
    maria_food = {}
    joao_food = {}
    joao_weekday = {}
    arnaldo_hamburger_ordered = 0
    joao_food_not_ordered = set()
    joao_weekday_not_ordered = set()
    data_list = []

    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    with open(path_to_file, encoding="utf-8") as csvfile:

        for food_item in food:
            maria_food[food_item] = 0
            joao_food[food_item] = 0

        data = csv.DictReader(csvfile, fieldnames = ['name', 'food', 'weekday'])

        for row in data:
            if row['food'] not in food:
                food.append(row['food'] )
                maria_food[ row['food'] ] = 0
                joao_food[ row['food'] ] = 0
            if row['weekday'] not in weekday:
                weekday.append(row['weekday'] )
                joao_weekday[ row['weekday'] ] = 0
            if row['name'] == 'maria':
                maria_food[ row['food'] ] += 1
            if row['name'] == 'joao':
                joao_food[ row['food'] ] += 1
            if row['name'] == 'joao':
                joao_weekday[ row['weekday'] ] += 1
            if row['name'] == 'arnaldo' and row['food'] == 'hamburguer':
                arnaldo_hamburger_ordered += 1

        max_ordered = max(maria_food , key=maria_food .get)
        for food_item in food:
            if joao_food[food_item] is 0:
                joao_food_not_ordered.add(food_item)
        for weekday_item in weekday:
            if joao_weekday[weekday_item] is 0:
                joao_weekday_not_ordered.add(weekday_item)

        print("maria max ordered", max_ordered)
        print("arnaldo_hamburger_ordered", arnaldo_hamburger_ordered)
        print('joao_food_not_ordered', joao_food_not_ordered)
        print('joao_weekday_not_ordered_list', joao_weekday_not_ordered)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{max_ordered}\n")
        file.write(f"{arnaldo_hamburger_ordered}\n")
        file.write(f"{joao_food_not_ordered}\n")
        file.write(f"{joao_weekday_not_ordered}")


