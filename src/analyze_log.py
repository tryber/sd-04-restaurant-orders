import csv
from statistics import mode


def analyze_log(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        data = csv.DictReader(csvfile, fieldnames=["nome", "prato", "dia"])

        arnaldo_ask_burguer = 0
        list_pratos_maria = []
        list_pratos_joao = set()
        list_todos_pratos = set()
        list_todos_dias = set()
        list_dias_joao = set()

        for i, row in enumerate(data):
            list_todos_pratos.add(row["prato"])
            list_todos_dias.add(row["dia"])
            if row["nome"] == "arnaldo" and row["prato"] == "hamburguer":
                arnaldo_ask_burguer += 1
            if row["nome"] == "maria":
                list_pratos_maria.append(row["prato"])
            if row["nome"] == "joao":
                list_pratos_joao.add(row["prato"])
                list_dias_joao.add(row["dia"])

        joao_nunca_comeu = set(list_todos_pratos) - set(list_pratos_joao)
        maria_pediu_mais = mode(list_pratos_maria)
        dias_joao_n_foi = set(list_todos_dias) - set(list_dias_joao)

        print(arnaldo_ask_burguer)

        txtFile = open("./data/mkt_campaign.txt", "w")
        txtFile.write(
            f"{maria_pediu_mais}\n"
            f"{arnaldo_ask_burguer}\n"
            f"{joao_nunca_comeu}\n"
            f"{dias_joao_n_foi}\n"
        )

