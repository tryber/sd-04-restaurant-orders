import csv


def analyze_log(path_to_file):

    with open(path_to_file) as file:
        file_reader = csv.reader(file)
        return file_reader
