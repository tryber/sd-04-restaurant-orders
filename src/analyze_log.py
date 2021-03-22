import csv

def read_csv(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise ValueError("Only .csv")
    try:
        with open(path_to_file, encoding="utf-8") as csv_file:
            return list(csv.reader(csv_file))
    except FileExistsError:
        return 'File not found'


def get_most_requested_by_maria(orders_list):
    foods_dict = dict()
    for name, food, day in orders_list:
        if name == 'maria':
            if food in foods_dict:
                foods_dict[food] += 1
            else:
                foods_dict[food] = 1
    return max(foods_dict, key=foods_dict.get)


def get_times_that_arnaldo_asked_for_burger(orders_list):
    number_of_times = 0
    for name, food, day in orders_list:
        if name == 'arnaldo' and food == 'hamburguer':
            number_of_times += 1
    return number_of_times


def get_foods_that_joao_never_asked(orders_list):
    never_asked_foods = set()
    asked_foods = set()
    for name, food, day in orders_list:
        if food not in asked_foods:
            never_asked_foods.add(food)
        if name == 'joao':
            if food in never_asked_foods:
                never_asked_foods.remove(food)
            asked_foods.add(food)
    return never_asked_foods


def get_days_that_joao_never_goes(orders_list):
    never_went_days = set()
    went_days = set()
    for name, food, day in orders_list:
        if day not in went_days:
            never_went_days.add(day)
        if name == 'joao':
            if day in never_went_days:
                never_went_days.remove(day)
            went_days.add(day)
    return never_went_days


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)
    most_requested_by_maria = get_most_requested_by_maria(orders)
    arnaldo_buger = get_times_that_arnaldo_asked_for_burger(orders)
    joao_never_asked = get_foods_that_joao_never_asked(orders)
    joao_never_went = get_days_that_joao_never_goes(orders)
    result = f"""{most_requested_by_maria};
{arnaldo_buger};
{joao_never_asked};
{never_went_days};
{joao_never_went}
"""
    print(result)
    return result
