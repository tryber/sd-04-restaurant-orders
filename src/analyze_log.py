import csv


def get_data_file(path_to_file):

    with open(path_to_file) as file:
        file_reader = csv.reader(file)
        data = [*file_reader]
        return data

    file.close()


def maria_most_ordered(data):

    maria_dishes_counter = dict()

    for order in data:
        if order[0] == "maria":
            if order[1] not in maria_dishes_counter:
                maria_dishes_counter[order[1]] = 1
            else:
                maria_dishes_counter[order[1]] += 1

    return max(maria_dishes_counter, key=maria_dishes_counter.get)


def arnaldo_ordered_burger(data):

    arnaldo_burger_counter = 0

    for order in data:
        if order[0] == "arnaldo" and order[1] == "hamburguer":
            arnaldo_burger_counter += 1

    return arnaldo_burger_counter


def joao_never_ordered(data):

    all_dishes = set()
    joao_dishes_ordered = set()

    for order in data:
        if order[1] not in all_dishes:
            all_dishes.add(order[1])
        if order[0] == "joao" and order[1] not in joao_dishes_ordered:
            joao_dishes_ordered.add(order[1])

    joao_not_ordered = all_dishes - joao_dishes_ordered

    return joao_not_ordered


def joao_never_went(data):

    all_days = set()
    joao_days_went = set()

    for order in data:
        if order[2] not in all_days:
            all_days.add(order[2])
        if order[0] == "joao" and order[2] not in joao_days_went:
            joao_days_went.add(order[2])

    joao_not_went = all_days - joao_days_went

    return joao_not_went


def analyze_log(path_to_file):

    data = get_data_file(path_to_file)

    file_writer = open("data/mkt_campaign.txt", "w")
    file_writer.write(f"{maria_most_ordered(data)}\n")
    file_writer.write(f"{arnaldo_ordered_burger(data)}\n")
    file_writer.write(f"{joao_never_ordered(data)}\n")
    file_writer.write(f"{joao_never_went(data)}\n")

    file_writer.close()


path_to_file = "data/orders_1.csv"
analyze_log(path_to_file)
