import csv
from collections import Counter


def never_days_joao(data):
    set_joao = set()
    set_resto = set()
    for order in data:
        if order[0] == "joao":
            set_joao.add(order[2])
        else:
            set_resto.add(order[2])
    return set_resto.difference(set_joao)


def never_order_joao(data):
    set_joao = set()
    set_resto = set()
    for order in data:
        if order[0] == "joao":
            set_joao.add(order[1])
        else:
            set_resto.add(order[1])
    return set_resto.difference(set_joao)


def quantity_of_arnaldo(data):
    lista = []
    for order in data:
        if order[0] == 'arnaldo' and order[1] == 'hamburguer':
            lista.append(order)
    return len(lista)


def more_request_maria(data):
    lista = []
    for order in data:
        if order[0] == 'maria':
            lista.append(order[1])
    most = Counter(lista)  # cria um contador
    biggest_value = max(most.values())
    # retorna o VALOR do maior contador
    biggest_keys = [key for key, value in most.items() if value ==
                    biggest_value]
    # faço um for in trazendo chave e valor e
    # retorno o que tem o mesmo valor maximo
    return biggest_keys[0]


def import_data(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    with open(path) as csv_file:
        data = []
        csv_reader = csv.reader(csv_file)
        for item in csv_reader:
            data.append(item)
        return data


def analyze_log(path_to_file):
    # if not path_to_file.endswith(".csv"):
    #     raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    data = import_data(path_to_file)
    maria = more_request_maria(data)
    arnaldo = quantity_of_arnaldo(data)
    joaoorders = never_order_joao(data)
    joaodays = never_days_joao(data)

    txt = open("data/mkt_campaign.txt", 'w')
    txt.write(f"{maria};\n{arnaldo};\n{joaoorders};\n{joaodays};")
    txt.close()
    return True
    # print(f"{maria};\n{arnaldo};\n{joaoorders};\n{joaodays};")


# path = "data/orders_1.csv"
# path = "data/orders_2.csv"
# analyze_log(path)
