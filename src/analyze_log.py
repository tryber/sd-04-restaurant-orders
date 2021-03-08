import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(
            "No such file or directory: " f"'{path_to_file}'"
        )

    orders = list()

    with open(path_to_file) as csv_file:
        orders_reader = csv.reader(csv_file, delimiter=",")
        for order in orders_reader:
            orders.append(order)

        csv_file.close
