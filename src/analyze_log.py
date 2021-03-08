# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# from collections import defaultdict
import operator
import csv


# Função para prato mais pedido -----------------------------------------
def get_favorite_meal(data, person):
    person_meals = {}

    for name, meal, day in data:
        if person == name:
            if meal not in person_meals:
                person_meals[meal] = 1
            else:
                person_meals[meal] += 1

    return max(person_meals.items(), key=operator.itemgetter(1))[0]


# Função quantidade de vezes que o prato foi pedido-----------------------
def get_meal_qty(data, person, order):
    qty = 0

    for name, meal, day in data:
        if person == name and order == meal:
            qty += 1

    return qty


# Função para pratos NÃO pedidos -----------------------------------------
def get_unordered_meals(data, person):
    all_meals = set()
    person_meals = set()

    for name, meal, day in data:
        all_meals.add(meal)

        if person == name:
            person_meals.add(meal)

    return all_meals.difference(person_meals)


# Função para dias NÃO idos ---------------------------------------------
def get_ungone_days(data, person):
    all_days = set()
    gone_days = set()

    for name, meal, day in data:
        all_days.add(day)

        if person == name:
            gone_days.add(day)

    return all_days.difference(gone_days)


def analyze_log(path_to_file):
    with open(path_to_file, "r") as file:
        content = csv.reader(file, delimiter=",")
        data = list(content)

    with open("data/mkt_campaign.txt", "w") as analyze_file:
        analyze_file.write(f"{get_favorite_meal(data, 'maria')}\n")
        analyze_file.write(f"{get_meal_qty(data, 'arnaldo', 'hamburguer')}\n")
        analyze_file.write(f"{get_unordered_meals(data, 'joao')}\n")
        analyze_file.write(f"{get_ungone_days(data, 'joao')}")
