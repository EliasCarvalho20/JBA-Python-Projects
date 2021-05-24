from .Tables import Table


class Recipes(Table):
    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)
        self.table_name = "recipe"

    def create_table(self) -> None:
        self.db.create_connection()
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name}s ("
            f"{self.table_name}_id INTEGER PRIMARY KEY, {self.table_name}_name TEXT NOT NULL, "
            f"{self.table_name}_description TEXT);"
        )

        self.db.execute_query(query)
        self.db.connection.commit()

    def populate(self, recipe_name: str, recipe_description: str) -> int:
        query = (
            f"INSERT INTO {self.table_name}s ({self.table_name}_name, {self.table_name}_description) "
            f"VALUES ('{recipe_name}', '{recipe_description}');"
        )

        self.db.execute_query(query)
        self.db.connection.commit()
        return self.db.cursor.lastrowid
