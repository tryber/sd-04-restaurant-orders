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


def most_requested(orders_list, client):
    count_orders = {}
    mais_pedido = orders_list[0][1]
    for order in orders_list:
        # checa cliente
        if order[0] == client:
            # conta pedido
            if order[1] not in count_orders:
                count_orders[order[1]] = 1
            else:
                count_orders[order[1]] += 1

            # pegar o mais pedido
            if count_orders[order[1]] > count_orders[mais_pedido]:
                mais_pedido = count_orders[order[1]]

    return mais_pedido


def count_foods(orders_list, client, food):
    count_burguers = 0
    for order in orders_list:
        if order[0] == client:
            if order[1] == food:
                count_burguers += 1

    return count_burguers


def nada_feito(orders_list, client, food_or_day):
    super_set = set()
    sub_set = set()

    for order in orders_list:
        super_set.add(order[food_or_day])
        if order[0] == client:
            sub_set.add(order[food_or_day])

    client_never_done = super_set.difference(sub_set)
    return client_never_done


def analyze_log(path_to_file):
    orders_list = read_file_csv(path_to_file)

    mais_pedido_maria = most_requested(orders_list, "maria")

    arnaldo_hamburguer = count_foods(orders_list, "arnaldo", "hamburguer")

    joao_nunca_pediu = nada_feito(orders_list, "joao", 1)

    joao_nunca_foi = nada_feito(orders_list, "joao", 2)

    with open("data/mkt_campaign.txt", "w") as log:
        log.write(f"{mais_pedido_maria}\n")
        log.write(f"{arnaldo_hamburguer}\n")
        log.write(f"{joao_nunca_pediu}\n")
        log.write(f"{joao_nunca_foi}\n")
