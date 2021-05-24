from .Tables import Table


class Quantity(Table):
    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)
        self.table_name = "quantity"

    def create_table(self) -> None:
        self.db.create_connection()
        query = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
            f"{self.table_name}_id INTEGER PRIMARY KEY, "
            f"{self.table_name} INTEGER NOT NULL, measure_id INTEGER NOT NULL, "
            "recipe_id INTEGER NOT NULL, ingredient_id INTEGER NOT NULL, "
            "FOREIGN KEY (measure_id) "
            "REFERENCES measures (measure_id), "
            "FOREIGN KEY (recipe_id) "
            "REFERENCES recipes (recipe_id), "
            "FOREIGN KEY (ingredient_id) "
            "REFERENCES ingredients (ingredient_id));"
        )

        self.db.execute_query(query)
        self.db.connection.commit()

    def populate(
        self, quantity: int, measure: str, ingredients: str, recipe_id: int
    ) -> None:
        measure_id = self.get_by_id("measure", measure)
        ingredient_id = self.get_by_id("ingredient", ingredients)

        query = (
            f"INSERT INTO {self.table_name} (quantity, recipe_id, measure_id, ingredient_id) "
            f"VALUES ({quantity}, {recipe_id}, {measure_id}, {ingredient_id});"
        )

        self.db.execute_query(query)
        self.db.connection.commit()
