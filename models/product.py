from datetime import datetime


class Product(object):
    Id = None
    Stock = None
    DateTime = None

    def __init__(self, id, stock):
        self.Id = int(id)
        self.Stock = float(stock)
        self.DateTime = str(datetime.utcnow())

    def get_data(self):
        return self.Id, self.Stock, self.DateTime
