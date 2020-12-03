import sqlite3


def create_new_customer(connection, cursor, data):   
    try:          
        sql = "insert into products(id, name, age, avatar) values(?,?,?,?)"
        cursor.execute(sql, data)
        connection.commit()       
    except Exception as error:
        print("ErrorCreate", error)
    finally:
        cursor.close()
        connection.close()


def delete_customer(connection, cursor, id):  
    try:
        sql = "delete from customers where code = 1"
        cursor.execute(sql, id)
        connection.commit()
        if cursor.rowcount > 0:
            deleted = True
        else:
            deleted = False
    except Exception as error:
        print("ErrorDelete", error))
    finally:
        cursor.close()
        connection.close()

    return deleted

def retrieve_single_customer(connection, cursor, id):
    try:
        sql = "select * from customer where id = ?"
        cursor.execute(sql, id)
        customer = cursor.fetchone()
        if customer is None:
            state = False

    except Exception as error:
        print("ErrorRetrievingProduct: " + str(error))

    finally:
        cursor.close()
        connection.close()

    return


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
