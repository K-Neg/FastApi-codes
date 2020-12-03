import sqlite3

class Products_Manager():
    def __init__(self):
        pass

    def insert_produtos():
        code = str(input("Digite o code do produto: "))
        description = str(input("Digite a descrição do produto: "))
        price = str(input("Digite o preço do produto: "))

        try:
            conexao = sqlite3.connect('shop.db')  # cria e/ou conecta
            cursor = conexao.cursor()
            sql = "insert into products(code,description,price) values(?,?,?)"
            cursor.execute(sql, [code, description, price])
            conexao.commit()
            print("Product "+description+" inserted!")

        except Exception as erro:
            print("Insertion failed: "+str(erro))

        finally:
            cursor.close()
            conexao.close()

    def excluir_produto():
        code = int(input("Digite o codigo do produto: "))

        try:
            connection = sqlite3.connect("shop.db")  # cria e/ou conecta
            cursor = connection.cursor()
            sql = "delete from produtos where code = ?"
            cursor.execute(sql, (code))
            connection.commit()
            if cursor.rowcount > 0:
                print("produto excluido com sucesso!")
            else:
                print("Produto não encontrado")

        except Exception as error:
            print("Falha: " + str(error))

        finally:
            cursor.close()
            connection.close()

    def read_all_products():
        
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
