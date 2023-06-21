__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"


import sqlite3 as sql

class Database:
    def __init__(self, path: str=None) -> None:
        if not path:
            raise Exception("Error connecting to database! Error: Name of database not specified.")
        try:
            self.connection = sql.connect(path)
        except sql.Error as e:
            raise Exception(f"Error connecting to database! Error: {e}")

class Saves(object):
    def __init__(self, database: Database) -> None:
        self.connection = database.connection
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS saves (
                slot INTEGER PRIMARY KEY,
                username TEXT,
                playertype INTEGER,
                chunk_x INTEGER,
                chunk_y INTEGER,
                world_x INTEGER,
                world_y INTEGER
            )
            '''
        )

    def save(self, slot: int, username: str, playertype: int, chunk_position: tuple, world_position: tuple) -> None:
        # Delete any existing data for the given slot
        self.cursor.execute('DELETE FROM saves WHERE slot = ?', (slot,))
        
        chunk_x, chunk_y = chunk_position
        world_x, world_y = world_position

        # Insert the new data
        self.cursor.execute('INSERT INTO saves (slot, username, playertype, chunk_x, chunk_y, world_x, world_y) VALUES (?, ?, ?, ?, ?, ?, ?)', (slot, username, playertype, chunk_x, chunk_y, world_x, world_y))
        self.connection.commit()

    def load(self, slot: int) -> tuple:
        # get data for the given slot
        self.cursor.execute('SELECT * FROM saves WHERE slot = ?', (slot,))
        row = self.cursor.fetchone()

        if row is not None:
            _, username, playertype, chunk_x, chunk_y, world_x, world_y = row
            return username, playertype, chunk_x, chunk_y, world_x, world_y
        else:
            return None
        
    def load_all(self):
        self.cursor.execute('SELECT * FROM saves')
        rows = self.cursor.fetchall()

        data = []
        for row in rows:
            if row:
                slot, username, playertype, chunk_x, chunk_y, world_x, world_y = row
                data.append((slot, username, playertype, chunk_x, chunk_y, world_x, world_y))
        return data
    
    def delete(self, slot):
        self.cursor.execute('DELETE FROM saves WHERE slot = ?', (slot,))
        self.connection.commit()

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()