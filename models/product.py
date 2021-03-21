from datetime import datetime


class Product(object):
    Reference = None
    Stock = None
    DateTime = None

    def __init__(self, Reference, stock):
        self.Reference = Reference
        self.Stock = float(stock)
        self.DateTime = str(datetime.utcnow())

    def get_data(self):
        return self.Reference, self.Stock, self.DateTime
