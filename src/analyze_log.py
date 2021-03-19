import csv


def maria_mais_pedido(data):
    pedidos = []
    maior = set()
    for line in data:
        if line[0] == 'maria':
            pedidos.append(line[1])
    for pedido in pedidos:
        maior.add((pedidos.count(pedido), pedido))
        maior2 = dict(maior)
    return maior2[max(maior2)]


def arnaldo_burgao(data):
    pedidos = []
    for line in data:
        if line[0] == 'arnaldo':
            pedidos.append(line[1])
    return pedidos.count('hamburguer')


def joao_nunca_comeu(data):
    pedidos = set()
    pedidos_joao = set()
    for line in data:
        if line[0] == 'joao':
            pedidos_joao.add(line[1])
        else:
            pedidos.add(line[1])
    return pedidos - pedidos_joao


def joao_nunca_foi(data):
    dias = set()
    dias_joao = set()
    for line in data:
        if line[0] == 'joao':
            dias_joao.add(line[2])
        else:
            dias.add(line[2])
    return dias - dias_joao


def import_data(caminho):
    try:
        result = []
        with open(caminho) as file:
            reader = csv.reader(file, delimiter='\n')
            for line in reader:
                newline = line[0].split(',')
                result.append(newline)
            return result
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{caminho}'")


def analyze_log(path_to_file):

    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    data = import_data(path_to_file)
    data_maria = maria_mais_pedido(data)
    data_arnaldo = arnaldo_burgao(data)
    data_jmenu = joao_nunca_comeu(data)
    data_jdias = joao_nunca_foi(data)

    txt = open("data/mkt_campaign.txt", 'w')
    txt.write(f"{data_maria}\n{data_arnaldo}\n{data_jmenu}\n{data_jdias}")
    txt.close()
    return True


# caminho = "data/orders_1.csv"
# caminho2 = "data/orders_1.txt"

# print(analyze_log(caminho2))
