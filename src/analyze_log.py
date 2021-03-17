from collections import defaultdict
from collections import Counter
import csv


def analyze_log(path_to_file):
    # caminho csv
    file = path_to_file

    # criando conjuntos por pessoa,
    # por tipo de comida e dia da semana
    conj_arnaldo = defaultdict(list)
    conj_joao = defaultdict(list)
    conj_maria = defaultdict(list)
    conj_food = set()
    con_day = set()

    if not file.endswith(".csv"):
        raise ValueError("Formato invalido")
    # separando o csv por conjuntos
    with open(file) as f:
        file_text = csv.reader(f, delimiter=",", quotechar='"')
        for name, food, day in file_text:
            # conjuntos tipo de comida e dia da semana
            conj_food.add(food)
            con_day.add(day)
            # conjuntos por pessoa
            if name == 'maria':
                conj_maria['maria'].append(food)
            elif name == 'joao':
                conj_joao['joao'].append(food)
                conj_joao['joao'].append(day)
            elif name == 'arnaldo':
                conj_arnaldo['arnaldo'].append(food)

    # Prato mais pedido por maria
    maria_count_food = Counter(conj_maria['maria'])
    maria_max_food = max(maria_count_food, key=maria_count_food.get)
    print(maria_max_food)

    # Quantas vezes 'arnaldo' pediu 'hamburguer'
    arnaldo_count_food = Counter(conj_arnaldo['arnaldo'])
    arnaldo_qtd_hamburguer = arnaldo_count_food['hamburguer']
    print(arnaldo_qtd_hamburguer)

    # Quais pratos 'joao' nunca pediu
    joao_food = conj_food.difference(conj_joao['joao'])

    # Quais dias 'joao' nunca foi na lanchonete
    joao_day = con_day.difference(conj_joao['joao'])

    # criando arquivo csv
    with open('../data/mkt_campaign.txt', 'w') as writer_csv:
        writer_csv = csv.writer(writer_csv, delimiter=';')
        writer_csv.writerow([maria_max_food])
        writer_csv.writerow([arnaldo_qtd_hamburguer])
        writer_csv.writerow([joao_food])
        writer_csv.writerow([joao_day])
        
# analyze_log('../data/orders_1.csv')
