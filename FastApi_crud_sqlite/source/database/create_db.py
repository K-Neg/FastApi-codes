import sqlite3


def create_customer_table():
    try:
        connection = sqlite3.connect("shop.db")  # creates or connect to it
        cursor = connection.cursor()
        sql = "create table if not exists customer(user_id integer PRIMARY KEY, name text , age integer, avatar text)"
        cursor.execute(sql)
        print("Table created!")

    except Exception as erro:
        print("Table creation fail: " + str(erro))

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_customer_table()
