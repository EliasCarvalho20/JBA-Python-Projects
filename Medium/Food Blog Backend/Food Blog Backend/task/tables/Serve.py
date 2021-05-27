from .Tables import Table


class Serve(Table):
    def __init__(self, table_name: str, db_name: str) -> None:
        super().__init__(table_name, db_name)

    def create_table(self) -> None:
        self.db.create_connection()
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"{self.table_name}_id INTEGER PRIMARY KEY, "
            "meal_id INTEGER NOT NULL, recipe_id INTEGER NOT NULL, "
            "FOREIGN KEY (meal_id) "
            "REFERENCES meals (meal_id), "
            "FOREIGN KEY (recipe_id) "
            "REFERENCES recipes (recipe_id));"
        )

        self.db.execute_query(query)
        self.db.connection.commit()

    def populate(self, meal_id: list, recipe_id: int) -> None:
        for m in meal_id:
            query = (
                f"INSERT INTO {self.table_name} (meal_id, recipe_id) "
                f"VALUES ({m}, {recipe_id});"
            )
            self.db.execute_query(query)

        self.db.connection.commit()
