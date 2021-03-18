import csv
from models.product import Product


class Parser(object):
    path = None

    def __init__(self, file_path):
        self.path = file_path

    def parse(self):
        with open(self.path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
                return Product(row[0], row[1])
