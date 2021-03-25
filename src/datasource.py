import csv


def parse_data(path_to_file):
    datasource = []

    with open(path_to_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=[
                                'name', 'food', 'week_day'])

        for line in reader:
            datasource.append(line)

    return datasource
