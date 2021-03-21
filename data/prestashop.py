import mysql.connector
import config


class PrestaShopDB(object):
    def __init__(self):
        self.presta_connection = mysql.connector.connect(
            host=config.ECOM_DB_HOST,
            user=config.ECOM_DB_USER,
            password=config.ECOM_DB_PASSWORD,
            database=config.ECOM_DB_NAME
        )

        self.presta_cursor = self.presta_connection.cursor()

    def update_quantity(self, reference, quantity):
        sql = f"""
        update ps_stock_available 
        join ps_product_attribute on ps_stock_available.id_product_attribute = ps_product_attribute.id_product_attribute
        set ps_stock_available.quantity = {quantity}
        where ps_product_attribute.reference = '{reference}';
        """

        self.presta_cursor.execute(sql)

        if self.presta_cursor.rowcount > 1:
            print(f"Failed to update product, there is more than 1 product with the same reference: {reference} ")
            self.presta_connection.rollback()
            return

        self.presta_connection.commit()
        print(self.presta_cursor.rowcount, "record(s) affected")
