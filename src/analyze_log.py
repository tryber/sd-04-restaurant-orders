import csv
# from datasource import parse_data


def analyze_log(path_to_file):
    datasource = parse_data(path_to_file)
    output = (
        f"{person_favorite_food('maria', datasource)}\n"
        f"{food_order_count('arnaldo', 'hamburguer', datasource)}\n"
        f"{no_orders('food' ,'joao', datasource)}\n"
        f"{no_orders('week_day' ,'joao', datasource)}"
    )

    output_to_file(output, './data/mkt_campaign.txt')


def person_favorite_food(person_name, datasource):
    person_foods_list = [data['food']
                         for data in datasource if data['name'] == person_name]
    favorite_food = max(person_foods_list, key=person_foods_list.count)

    return favorite_food


def food_order_count(person_name, food, datasource):
    food_order_list = [data['food'] for data in datasource if data['name']
                       == person_name and data['food'] == food]

    return len(food_order_list)


def no_orders(field, person_name, datasource):
    avaible = set([data[field] for data in datasource])
    have_orders = set([data[field]
                      for data in datasource if data['name'] == person_name])
    no_ordered = avaible.difference(have_orders)

    return no_ordered


def parse_data(path_to_file):
    datasource = []

    with open(path_to_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=[
                                'name', 'food', 'week_day'])

        for line in reader:
            datasource.append(line)

    return datasource


def output_to_file(output, file_path):
    with open(file_path, "w") as text_file:
        text_file.write(output)
