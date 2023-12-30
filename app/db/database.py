import sqlite3
from app.classes.animal import Animal

class Database:
    def __init__(self, db_path):
        self.connetion = sqlite3.connect(db_path)
        self.cursor = self.connetion.cursor()
        self.create_tables()


    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                species TEXT NOT NULL
            )
        ''')

    def add_animal(self, animal):
        self.cursor.execute('''
            INSERT INTO animals (name, species)
            VALUES (?, ?)
        ''', (animal.name, animal.species))
        self.connetion.commit()

    def get_all_animals(self):
        self.cursor.execute('SELECT * FROM animals')
        return self.cursor.fetchall()

    def close_connection(self):
        self.connetion.close()