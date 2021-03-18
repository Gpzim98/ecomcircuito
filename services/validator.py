from os import path
from os import stat


class Validator(object):
    path = None

    def __init__(self, path):
        self.path = path

    def is_valid(self):
        exist = path.exists(self.path)
        not_empty = stat(self.path).st_size > 0
        return exist and not_empty
