import csv
from statistics import mode


def write_save(maria, arnaldo, all_foods, all_days, joao_foods, joao_days):
    with open('data/mkt_campaign.txt', "w") as save:
        save.write(f"{mode(maria)}\n")
        save.write(f"{arnaldo}\n")
        save.write(f"{set(all_foods) - set(joao_foods)}\n")
        save.write(f"{set(all_days) - set(joao_days)}\n")


def arnaldo_sum(st, arnaldo_burguer):
    if st['nome'] == "arnaldo" and st['prato'] == "hamburguer":
        arnaldo_burguer += 1
    return arnaldo_burguer


def analyze_log(path_to_file):
    if not path_to_file.endswith("csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    maria_food = []
    arnaldo_burguer = 0
    all_foods = set()
    joao_foods = set()
    all_days = set()
    joao_days = set()

    with open(path_to_file, newline="") as file:
        store = csv.DictReader(file, fieldnames=["nome", "prato", "dia"])

        for index, store_type in enumerate(store):
            all_days.add(store_type["dia"])
            all_foods.add(store_type["prato"])
            if store_type["nome"] == "maria":
                maria_food.append(store_type["prato"])
            arnaldo_burguer = arnaldo_sum(store_type, arnaldo_burguer)
            if store_type["nome"] == "joao":
                joao_days.add(store_type["dia"])
                joao_foods.add(store_type["prato"])

    write_save(
        maria_food, arnaldo_burguer,
        all_foods, all_days,
        joao_foods, joao_days)
