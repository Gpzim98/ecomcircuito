from models.product import Product
import sqlite3
import config


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print("Failed to create connection" + e)

    return conn


class DataBase(object):
    conn = None

    def __init__(self):
        database = config.DB_NAME

        self.conn = create_connection(database)

    def store_product(self, project: Product):
        try:
            sql = "INSERT INTO InventoryControl(Reference, Stock, DateTime) VALUES(?,?,?)"
            cur = self.conn.cursor()
            cur.execute(sql, project.get_data())
            self.conn.commit()
            print("Product successfully stored")
            return True
        except Exception as e:
            print("Failed to insert into InventoryControl " + str(e))
            return False
