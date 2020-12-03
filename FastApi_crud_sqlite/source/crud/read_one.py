import sqlite3


def retrieve_single_product(code):
    code = code
    # code = int(input("Digite o codigo do produto: "))

    try:
        connection = sqlite3.connect("shop.db")  # cria e/ou conecta
        cursor = connection.cursor()
        sql = "select * from products where code = ?"
        cursor.execute(sql, str(code))
        product = cursor.fetchone()
        if product is None:
            print("produto não localizado!")
            return False
        else:
            print(product[0], product[1], product[2])
            return product

    except Exception as error:
        print("ErrorRetrievingProduct: " + str(error))

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    retrieve_single_product()
