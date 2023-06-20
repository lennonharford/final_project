import sqlite3 as sql

class Database:
    def __init__(self, path: str=None) -> None:
        if not path:
            raise Exception("Error connecting to database! Error: Name of database not specified.")
        try:
            self.connection = sql.connect(path)
        except sql.Error as e:
            raise Exception(f"Error connecting to database! Error: {e}")
    
class Table:
    def __init__(self, parent: Database, title: str, *columns: str) -> None:
        try:
            self.connection = parent.connection
            self.cursor = self.connection.cursor()
        except sql.Error as e:
            raise Exception(f"Error connecting to database! Error: {e}")
        
        self.title = title
        self.columns = columns
        
        variables = ','.join(self.columns)
        
        self.connection.execute(
            f'''
            CREATE TABLE IF NOT EXISTS {self.title}(
                id INTEGER PRIMARY KEY, 
                {variables}
            );
            '''
        )
        self.connection.commit()
        
    def data(self) -> list:
        data = self.connection.execute(
            f'''
            SELECT * from {self.title};
            '''
        ).fetchall()
        
        return list(map(list, data))
        
    def insert(self, columns, data):
        self.connection.execute(
            f'''
            INSERT INTO {self.title} {tuple(columns)} VALUES {tuple(data)};
            '''
        )
        self.connection.commit()
        
    def remove(self, column, data) -> None:
        self.connection.execute(
            f'''
            DELETE FROM {self.title} WHERE {column} = '{data}';
            '''
        )
        self.connection.commit()
        
    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
