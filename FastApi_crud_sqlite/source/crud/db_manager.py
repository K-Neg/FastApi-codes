import sqlite3

class ModelSQLite():
    def __init__(self):
        self.connection = sqlite3.connect('shop.db') 
        self.cursor = connection.cursor()

    def create_new_customer():
        