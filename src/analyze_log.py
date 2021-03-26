import csv


def most_requested(data):
    request = []
    bigger = set()
    for line in data:
        if line[0] == 'maria':
            request.append(line[1])
    for pedido in request:
        bigger.add((request.count(pedido), pedido))
        great_bigger = dict(bigger)
    return great_bigger[max(great_bigger)]


def how_mutch(data):
    request = []
    for line in data:
        if line[0] == 'arnaldo':
            request.append(line[1])
    return request.count('hamburguer')


def never_eat(data):
    requested = set()
    request_user = set()
    for line in data:
        if line[0] == 'joao':
            request_user.add(line[1])
        else:
            requested.add(line[1])
    return requested - request_user


def never_comeback(data):
    days = set()
    days_user = set()
    for line in data:
        if line[0] == 'joao':
            days_user.add(line[2])
        else:
            days.add(line[2])
    return days - days_user


def import_data(path):
    try:
        result = []
        with open(path) as file:
            reader = csv.reader(file, delimiter='\n')
            for line in reader:
                newline = line[0].split(',')
                result.append(newline)
            return result
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    data = import_data(path_to_file)
    data_maria = most_requested(data)
    data_arnaldo = how_mutch(data)
    data_jmenu = never_eat(data)
    data_jdias = never_comeback(data)

    txt = open("data/mkt_campaign.txt", 'w')
    txt.write(f"{data_maria}\n{data_arnaldo}\n{data_jmenu}\n{data_jdias}")
    txt.close()
    return True
    