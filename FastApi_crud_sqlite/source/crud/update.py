import sqlite3
from read_one import retrieve_single_product


def update_produto():
    code = input("Codigo: ")
    product = retrieve_single_product(code)
    user_want_to_update = False

    if product:
        description = product[1]
        price = product[2]

        description_buffer = input(
            "Descrição atual: " + description + ", para manter digite ENTER --> "
        )

        if description_buffer != "":
            description = description_buffer
            user_want_to_update = True

        price_buffer = input(
            "Preço atual: " + str(price) + ", para manter digite ENTER --> "
        )
        if price_buffer != "":
            price = float(price_buffer)
            user_want_to_update = True

        if user_want_to_update:
            try:
                connection = sqlite3.connect("shop.db")  # cria e/ou conecta
                cursor = connection.cursor()
                sql = "update products set description = ?, price = ? where code = ?"
                cursor.execute(sql, (description, price, code))
                connection.commit()
                print("Produto " + description + " alterado com sucesso!")

            except Exception as error:
                print("ErrorUpdating: " + str(error), code)

            finally:
                cursor.close()
                connection.close()


if __name__ == "__main__":
    update_produto()
