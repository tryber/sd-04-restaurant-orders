import csv
from statistics import mode


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        data = csv.DictReader(file, fieldnames=["cliente", "pedido", "dia"])
        #  nomeando "colunas" com o parâmetro fieldnames

        maria_food = []
        arnaldo_burguer = 0
        joao_food = set()
        all_food = set()
        all_day = set()
        joao_day = set()

        for i, row in enumerate(data):
            all_food.add(row["pedido"])
            all_day.add(row["dia"])
            if row["cliente"] == "arnaldo" and row["pedido"] == "hamburguer":
                arnaldo_burguer += 1
            if row["cliente"] == "maria":
                maria_food.append(row["pedido"])
            if row["cliente"] == "joao":
                joao_food.add(row["pedido"])
                joao_day.add(row["dia"])

        joao_not_order = set(all_food) - set(joao_food)
        maria_favorite = mode(maria_food)
        not_order_day_joao = set(all_day) - set(joao_day)

        resultFile = open("./data/mkt_campaign.txt", "w")
        resultFile.write(
            f"{maria_favorite}\n"
            f"{arnaldo_burguer}\n"
            f"{joao_not_order}\n"
            f"{not_order_day_joao}\n"
        )
