from .database import Database

DATA = {
    "meals": ("breakfast", "brunch", "lunch", "supper"),
    "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar",),
    "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", ""),
}


class FoodBlog:
    def __init__(self) -> None:
        self.db = None
        self.TABLE_QUERIES = {}
        self.DATA_QUERY = {}
        self.recipes = {}

    def make_connection(self, filename: str) -> None:
        self.db = Database(filename)
        self.db.create_connection()

    def execute(self) -> None:
        self.create_data_queries()

        self.db.create_tables(self.TABLE_QUERIES)
        self.db.commit_changes()

        self.db.add_to_tables(DATA, self.DATA_QUERY)
        self.db.commit_changes()

    def create_data_queries(self) -> None:
        for key in DATA.keys():
            not_null = "NOT NULL UNIQUE" if key != "measures" else "UNIQUE"

            self.TABLE_QUERIES.update({
                key: f"CREATE TABLE IF NOT EXISTS {key} ("
                f"{key[:-1]}_id INTEGER PRIMARY KEY, {key[:-1]}_name TEXT {not_null});"
            })
            self.DATA_QUERY.update({
                key: f"INSERT INTO {key} ({key[:-1]}_name) VALUES (?);",
            })

        self.TABLE_QUERIES.update({
            "recipes": "CREATE TABLE IF NOT EXISTS recipes ("
            "recipe_id INTEGER PRIMARY KEY, recipe_name TEXT UNIQUE NOT NULL,"
            "recipe_description TEXT);",
        })

    def set_recipes(self, recipe_name: str, recipe_description: str) -> None:
        self.recipes.update({recipe_name: (recipe_name, recipe_description)})

    def create_recipes_query(self) -> None:
        insert_query = {
            key: "INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?);"
            for key in self.recipes.keys()
        }

        self.db.add_values_to_recipes(self.recipes, insert_query)
        self.db.commit_changes()
        self.db.close_connection()
