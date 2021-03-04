import csv


def read_file_csv(path_to_file):
    # Leitura de arquivo .csv
    try:
        with open(path_to_file) as path_csv:
            reader_csv = csv.reader(path_csv, delimiter=",", quotechar='"')
            orders_list = list(reader_csv)

    # lança erro caso arquivo seja inexistente
    # lança erro caso não seja .csv
    except FileExistsError:
        raise ValueError(f"No such file or directory: '{path_to_file}'")

    return orders_list


def most_requested_by_client(orders_list, client):
    count_orders = {}
    most_requested = orders_list[0][1]
    for order in orders_list:
        # checa cliente
        if order[0] == client:
            # conta pedido
            if order[1] not in count_orders:
                count_orders[order[1]] = 1
            else:
                count_orders[order[1]] += 1

            # pegar o mais pedido
            if count_orders[order[1]] > count_orders[most_requested]:
                most_requested = count_orders[1]

    return most_requested


def count_asked_food(orders_list, client, food):
    count_burguers = 0
    for order in orders_list:
        if order[0] == client:
            if order[1] == food:
                count_burguers += 1

    return count_burguers


def never_done(orders_list, client, food_or_day):
    # Superconjunto
    super_set = set()
    # subconjunto
    sub_set = set()

    for order in orders_list:
        super_set.add(order[food_or_day])
        if order[0] == "joao":
            sub_set.add(order[food_or_day])

    client_never_done = super_set.difference(sub_set)
    return client_never_done


def analyze_log(path_to_file):
    orders_list = read_file_csv(path_to_file)

    # A análise deve conter:
    # cliente, pedido, dia
    # 1. Qual o prato mais pedido por 'maria'?
    most_requested_by_maria = most_requested_by_client(orders_list, "maria")

    # 2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
    arnaldo_ask_hamburguer = count_asked_food(
        orders_list, "arnaldo", "hamburguer"
    )

    # 3. Quais pratos 'joao' nunca pediu?
    joao_never_asked = never_done(orders_list, "joao", 1)

    # 4. Quais dias 'joao' nunca foi na lanchonete?
    joao_never_went = never_done(orders_list, "joao", 2)

    # Cria um arquivo data/mkt_campaign.txt com a análise
    with open("data/mkt_campaign.txt", "w") as log:
        log.write(f"{most_requested_by_maria}\n")
        log.write(f"{arnaldo_ask_hamburguer}\n")
        log.write(f"{joao_never_asked}\n")
        log.write(f"{joao_never_went}\n")
