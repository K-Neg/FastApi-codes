import sqlite3


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


if __name__ == "__main__":
    inserir_produtos()
