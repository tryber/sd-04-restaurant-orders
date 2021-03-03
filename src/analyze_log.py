import csv
"""
Dados
    O atual sistema guarda os logs de todos os pedidos feitos em um arquivo csv, contendo o formato cliente, pedido, dia, um por linha e sem nome das colunas (a primeira linha já é um pedido).

    O log a ser utilizado é o arquivo data/orders_1.csv. Todas as informações são strings com letras minúsculas. O histórico contém pedidos feitos em todos os dias da semana e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio completo. Os dias da semana estão no formato "...-feira", "sabado" ou "domingo".
"""


def read_file_csv(path_to_file):
    # Leitura de arquivo .csv
    try:
        with open(path_to_file) as path_csv:
            reader_csv = csv.reader(path_csv, delimiter=",", quotechar='"')
            orders_list = list(reader_csv)
            print("ORDERS:", orders_list)
            # return orders_list
    # lança erro caso arquivo seja inexistente
    # lança erro caso não seja .csv
    except FileExistsError:
        raise ValueError("No such file or directory: '{path_to_file}'")

    return orders_list


def analyze_log(path_to_file):
    orders_list = read_file_csv(path_to_file)

    # A análise deve conter:
    # cliente, pedido, dia
    # 1. Qual o prato mais pedido por 'maria'?
    client = 'maria'
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
    print("Maria_Orders:", most_requested)

    # 2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
    # 3. Quais pratos 'joao' nunca pediu?
    # 4. Quais dias 'joao' nunca foi na lanchonete?
    # Cria um arquivo data/mkt_campaign.txt com a análise
    with open("data/mkt_campaign.txt ", "w") as log:
        log.write(f"{most_requested}\n")
