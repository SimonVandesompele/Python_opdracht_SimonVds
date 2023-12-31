import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                species TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zoos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL
            )
        ''')

    def add_animal(self, animal):
        self.cursor.execute('''
            INSERT INTO animals (name, species)
            VALUES (?, ?)
        ''', (animal.name, animal.species))
        self.connection.commit()

    def get_all_animals(self):
        self.cursor.execute('SELECT * FROM animals')
        return self.cursor.fetchall()

    def add_zoo(self, zoo):
        self.cursor.execute('''
            INSERT INTO zoos (name, location)
            VALUES (?, ?)
        ''', (zoo.name, zoo.location))
        self.connection.commit()

    def get_all_zoos(self):
        self.cursor.execute('SELECT * FROM zoos')
        return self.cursor.fetchall()

    def remove_animal(self, animal_id):
        self.cursor.execute('DELETE FROM animals WHERE id = ?', (animal_id,))
        self.connection.commit()

    def remove_zoo(self, zoo_id):
        self.cursor.execute('DELETE FROM zoos WHERE id = ?', (zoo_id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()