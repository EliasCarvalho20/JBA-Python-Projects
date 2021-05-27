from .Tables import Table


class Recipes(Table):
    def __init__(self, table_name: str, db_name: str) -> None:
        super().__init__(table_name, db_name)

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

    def get_recipes_by_ingredients(self, ingredients: list, meals: list) -> str:
        self.db.create_connection()
        ing_str = ", ".join(f"'{i}'" for i in ingredients)
        meals_str = ", ".join(f"'{m}'" for m in meals)

        query = (
            "SELECT r.recipe_name FROM recipes r "
            "INNER JOIN quantity q on r.recipe_id = q.recipe_id "
            "INNER JOIN serve s on s.recipe_id = r.recipe_id "
            "INNER JOIN ingredients i on i.ingredient_id = q.ingredient_id "
            "INNER JOIN meals m on m.meal_id = s.meal_id "
            f"WHERE i.ingredient_name IN ({ing_str}) "
            f"AND m.meal_name IN ({meals_str}) "
            "GROUP BY r.recipe_id "
            f"HAVING COUNT(r.recipe_id) = {len(ingredients)};"
        )

        self.db.execute_query(query)
        result = self.db.cursor.fetchall()

        if result:
            return f"Recipes selected for you: {', '.join(s[0] for s in result)}"

        return "There are no such recipes in the database."
