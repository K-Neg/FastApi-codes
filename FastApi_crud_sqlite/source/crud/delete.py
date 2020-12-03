import sqlite3


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
