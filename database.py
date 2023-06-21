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
                playertype INTEGER
            )
            '''
        )

    def save(self, slot: int, username: str, playertype: int) -> None:
        # Delete any existing data for the given slot
        self.cursor.execute('DELETE FROM saves WHERE slot = ?', (slot,))

        # Insert the new data
        self.cursor.execute('INSERT INTO saves (slot, username, playertype) VALUES (?, ?, ?)', (slot, username, playertype))
        self.connection.commit()

    def load(self, slot: int) -> tuple:
        # get data for the given slot
        self.cursor.execute('SELECT * FROM saves WHERE slot = ?', (slot,))
        row = self.cursor.fetchone()

        if row is not None:
            _, username, playertype = row
            return username, playertype
        else:
            return None
        
    def load_all(self):
        self.cursor.execute('SELECT * FROM saves')
        rows = self.cursor.fetchall()

        data = []
        for row in rows:
            if row:
                slot, username, playertype = row
                data.append((slot, username, playertype))
        return data
    
    def delete(self, slot):
        self.cursor.execute('DELETE FROM saves WHERE slot = ?', (slot,))
        self.connection.commit()

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()