from .Tables import Table


class Measure(Table):
    def __init__(self, table_name: str, db_name: str) -> None:
        super().__init__(table_name, db_name)

    def create_table(self) -> None:
        self.db.create_connection()
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name}s ("
            f"{self.table_name}_id INTEGER PRIMARY KEY, {self.table_name}_name TEXT UNIQUE);"
        )
        self.db.execute_query(query)
        self.db.connection.commit()
