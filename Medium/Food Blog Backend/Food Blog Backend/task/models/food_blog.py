from .database import Database

TABLES_QUERY = {
    "meals": (
        "CREATE TABLE IF NOT EXISTS meals ("
        "meal_id INTEGER PRIMARY KEY, meal_name TEXT NOT NULL UNIQUE);"
    ),
    "ingredients": (
        "CREATE TABLE IF NOT EXISTS ingredients ("
        "ingredient_id INTEGER PRIMARY KEY, ingredient_name TEXT NOT NULL UNIQUE);"
    ),
    "measures": (
        "CREATE TABLE IF NOT EXISTS measures ("
        "measure_id INTEGER PRIMARY KEY, measure_name TEXT UNIQUE);"
    ),
}

DATA = {
    "meals": ("breakfast", "brunch", "lunch", "supper"),
    "ingredients": (
        "milk",
        "cacao",
        "strawberry",
        "blueberry",
        "blackberry",
        "sugar",
    ),
    "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", ""),
}

DATA_QUERY = {
    "meals": "INSERT INTO meals (meal_name) VALUES (?);",
    "ingredients": "INSERT INTO ingredients (ingredient_name) VALUES (?);",
    "measures": "INSERT INTO measures (measure_name) VALUES (?);",
}


class FoodBlog:
    def __init__(self) -> None:
        self.db = None

    def make_connection(self, filename: str) -> None:
        self.db = Database(filename)
        self.db.create_connection()

    def execute(self) -> None:
        self.db.create_tables(TABLES_QUERY)
        self.db.add_to_tables(DATA, DATA_QUERY)
        self.db.commit_changes()
