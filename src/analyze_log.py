import csv
# https://stackoverflow.com/questions/14091636/get-dict-key-by-max-value


def open_csv_file(file_csv):
    try:
        with open(file_csv, 'r') as file:
            array_data = list()
            reader = csv.reader(file, delimiter=',')
            for item in reader:
                array_data.append(item)
            return array_data
    except FileExistsError:
        raise ValueError(f"No such file or directory: '{file_csv}'")


def set_obj(value):
    new_array = list()

    for item in value:
        temp_obj = {}
        temp_obj["client"] = item[0]
        temp_obj["order"] = item[1]
        temp_obj["day"] = item[2]
        new_array.append(temp_obj)
    return new_array


def count_orders_by_client(order_list, client):
    ordered = {}
    for item in order_list:
        food = item["order"]
        if item["client"] == client:
            if food not in ordered:
                ordered[food] = 1
            else:
                ordered[food] += 1
    return ordered


def most_ordered(obj):
    order = max(obj, key=obj.get)
    return order


def client_never_did(order_list, client, subj):
    original = set()
    modified = set()

    for order in order_list:
        original.add(order[subj])
        if (order[0]) == client:
            modified.add(order[subj])

    diff = original.difference(modified)
    return diff


def analyze_log(path_to_file):
    itens = open_csv_file(path_to_file)
    orders = set_obj(itens)

    maria_orders = count_orders_by_client(orders, "maria")
    first = most_ordered(maria_orders)

    arnaldo_orders = count_orders_by_client(orders, "arnaldo")
    second = arnaldo_orders['hamburguer']

    third = client_never_did(itens, "joao", 1)
    fourth = client_never_did(itens, 'joao', 2)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{first}\n")
        file.write(f"{second}\n")
        file.write(f"{third}\n")
        file.write(f"{fourth}\n")
