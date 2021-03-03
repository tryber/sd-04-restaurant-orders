import csv
"""
Dados
    O atual sistema guarda os logs de todos os pedidos feitos em um arquivo csv, contendo o formato cliente, pedido, dia, um por linha e sem nome das colunas (a primeira linha já é um pedido).

    O log a ser utilizado é o arquivo data/orders_1.csv. Todas as informações são strings com letras minúsculas. O histórico contém pedidos feitos em todos os dias da semana e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio completo. Os dias da semana estão no formato "...-feira", "sabado" ou "domingo".
"""

def analyze_log(path_to_file):
    # Leitura de arquivo .csv
    try:
        with open(path_to_file) as path_csv:
            reader_csv = csv.reader(path_csv, delimiter=",", quotechar='"')
            csv_list = list(reader_csv)
            print("CSV:", csv_list)
            return csv_list
    # lança erro caso arquivo seja inexistente
    # lança erro caso não seja .csv
    except FileExistsError:
        raise ValueError(f"No such file or directory: " "'{path_to_file}'")
    # A análise deve conter:
    # 1. Qual o prato mais pedido por 'maria'?
    # 2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
    # 3. Quais pratos 'joao' nunca pediu?
    # 4. Quais dias 'joao' nunca foi na lanchonete?
    # Cria um arquivo data/mkt_campaign.txt com a análise
    raise NotImplementedError
