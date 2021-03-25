import csv
# https://stackoverflow.com/questions/14091636/get-dict-key-by-max-value


def open_csv_file(file_csv):
    if not file_csv.endswith(".csv"):
        raise ValueError("Arquivo com extensão incorreta")
    else:
        with open(file_csv, 'r') as file:
            array_data = list()
            reader = csv.reader(file, delimiter=',')
            for item in reader:
                array_data.append(item)
            # print(array_data)
            return array_data


def set_obj(value):
    new_array = list()

    for item in value:
        temp_obj = {}
        temp_obj["client"] = item[0]
        temp_obj["order"] = item[1]
        temp_obj["day"] = item[2]
        new_array.append(temp_obj)
    # print(new_array)
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
    # print(ordered)
    return ordered


def most_ordered(obj):
    loo = max(obj, key=obj.get)
    return loo


def analyze_log(path_to_file):
    itens = open_csv_file(path_to_file)
    orders = set_obj(itens)

    maria_orders = count_orders_by_client(orders, "maria")
    first = most_ordered(maria_orders)
    print(first)

    arnaldo_orders = count_orders_by_client(orders, "arnaldo")
    second = arnaldo_orders['hamburguer']
    print(second)
