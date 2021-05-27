import sys
import os

from abc import ABC

sys.path.insert(0, os.path.abspath(".."))

from models.database import DBConnection


class Table(ABC):
    def __init__(self, table_name: str, db_name: str) -> None:
        self.table_name = table_name
        self.db = DBConnection(db_name)

    def create_table(self) -> None:
        self.db.create_connection()
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name}s ("
            f"{self.table_name}_id INTEGER PRIMARY KEY, {self.table_name}_name TEXT NOT NULL UNIQUE);"
        )

        self.db.execute_query(query)
        self.db.connection.commit()

    def populate_table(self, data: list) -> None:
        query = f"INSERT INTO {self.table_name}s ({self.table_name}_name) VALUES (?);"

        self.db.execute_many(query, data)
        self.db.connection.commit()

    def get_by_id(self, table_name: str, value_name: str) -> int:
        query = (
            f"SELECT {table_name}_id FROM {table_name}s WHERE {table_name}_name = ?;"
        )
        self.db.select_one(query, value_name)
        return self.db.cursor.fetchone()[0]
