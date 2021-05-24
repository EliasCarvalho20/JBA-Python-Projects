from .Tables import Table


class Meals(Table):
    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)
        self.table_name = "meal"

    def get_all_meals(self) -> list:
        self.db.create_connection()
        meals_query = "SELECT meal_id, meal_name FROM meals"

        self.db.select_all(meals_query)
        return self.db.cursor.fetchall()
