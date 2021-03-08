import csv


def csv_file_reader(path_to_file):
    try:
        with open(path_to_file) as path_csv:
            reader_csv = csv.reader(path_csv, delimiter=",", quotechar='"')
            orders_list = list(reader_csv)

    except FileExistsError:
        raise ValueError(f"No such file or directory: '{path_to_file}'")

    return orders_list


def most_ordered_by_client(orders_list, client):
    count_orders = {}
    most_ordered = orders_list[0][1]
    for order in orders_list:
        # checa cliente
        if order[0] == client:
            # conta pedido
            if order[1] not in count_orders:
                count_orders[order[1]] = 1
            else:
                count_orders[order[1]] += 1

            # pegar o mais pedido
            if count_orders[order[1]] > count_orders[most_ordered]:
                most_ordered = count_orders[order[1]]

    return most_ordered


def ordered_dish_counter(orders_list, client, dish):
    count_dish = 0
    for order in orders_list:
        if order[0] == client:
            if order[1] == dish:
                count_dish += 1

    return count_dish


def do_not_have_order(orders_list, client, dish):
    super_set = set()
    sub_set = set()

    for order in orders_list:
        super_set.add(order[dish])
        if order[0] == client:
            sub_set.add(order[dish])

    dont_have_order = super_set.difference(sub_set)

    return dont_have_order


def analyse_log(path_to_file):
    orders_list = csv_file_reader(path_to_file)

    # 1. Qual o prato mais pedido por 'maria'?
    most_ordered_by_maria = most_ordered_by_client(orders_list, "maria")

    # 2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
    arnaldo_ordered_hamburguer = ordered_dish_counter(
        orders_list, "arnaldo", "hamburguer"
    )

    # 3. Quais pratos 'joao' nunca pediu?
    joao_never_ordered = do_not_have_order(orders_list, "joao", 1)

    # 4. Quais dias 'joao' nunca foi na lanchonete?
    days_joao_did_not_go = do_not_have_order(orders_list, "joao", 2)

    # Cria um arquivo data/mkt_campaign.txt com a análise
    with open("data/mkt_campaign.txt", "w") as log:
        log.write(f"{most_ordered_by_maria}\n")
        log.write(f"{arnaldo_ordered_hamburguer}\n")
        log.write(f"{joao_never_ordered}\n")
        log.write(f"{days_joao_did_not_go}\n")
