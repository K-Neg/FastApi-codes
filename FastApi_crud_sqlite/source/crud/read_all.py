import sqlite3


def read_all_products():
    try:
        connection = sqlite3.connect('shop.db')
        cursor = connection.cursor()
        sql = "select * from products order by price desc"
        cursor.execute(sql)
        product_list = cursor.fetchall()
        for product in product_list:
            print(product[0], product[1], product[2])

    except Exception as error:
        print("Fail: "+str(error))

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    read_all_products()
