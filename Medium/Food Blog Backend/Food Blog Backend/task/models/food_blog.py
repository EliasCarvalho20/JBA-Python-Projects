from .database import Database

DATA = {
    "meals": [("breakfast",), ("brunch",), ("lunch",), ("supper",)],
    "ingredients": [("milk",), ("cacao",), ("strawberry",), ("blueberry",), ("blackberry",), ("sugar",)],
    "measures": [("ml",), ("g",), ("l",), ("cup",), ("tbsp",), ("tsp",), ("dsp",), ("",)],
}


class FoodBlog:
    def __init__(self) -> None:
        self.DB = Database()
        self.table_queries = {}
        self.data_query = {}
        self.recipes = {}

    def execute(self) -> None:
        self.create_table_and_data_queries()

        self.DB.create_tables(self.table_queries)
        self.DB.add_to_tables(self.data_query, DATA)

        self.DB.commit_changes()

    def create_table_and_data_queries(self) -> None:
        for key in DATA.keys():
            not_null = "NOT NULL UNIQUE" if key != "measures" else "UNIQUE"

            self.table_queries.update({
                key: f"CREATE TABLE IF NOT EXISTS {key} ("
                f"{key[:-1]}_id INTEGER PRIMARY KEY, {key[:-1]}_name TEXT {not_null});"
            })
            self.data_query.update({
                key: f"INSERT INTO {key} ({key[:-1]}_name) VALUES (?);",
            })

        self.table_queries.update({"recipes": self.create_table_recipes()})
        self.table_queries.update({"serve": self.create_table_serve()})

    @staticmethod
    def create_table_recipes() -> str:
        return (
            "CREATE TABLE IF NOT EXISTS recipes ("
            "recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, "
            "recipe_description TEXT);"
        )

    @staticmethod
    def create_table_serve() -> str:
        return (
            "CREATE TABLE IF NOT EXISTS serve ("
            "serve_id INTEGER PRIMARY KEY, "
            "meal_id INTEGER NOT NULL, recipe_id INTEGER NOT NULL, "
            "FOREIGN KEY (meal_id) "
            "REFERENCES meals (meal_id), "
            "FOREIGN KEY (recipe_id) "
            "REFERENCES recipes (recipe_id));"
        )

    def set_recipes(self, recipe_name: str, recipe_description: str) -> None:
        self.recipes = {recipe_name: [(recipe_name, recipe_description)]}

    def create_recipes_query(self) -> None:
        insert_query = {
            key: "INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?);"
            for key in self.recipes.keys()
        }

        self.DB.add_to_tables(insert_query, self.recipes)
        self.DB.commit_changes()

    def get_meals(self) -> list:
        meals_query = "SELECT meal_id, meal_name FROM meals"
        return self.DB.get_meals(meals_query)

    def get_recipe_id(self, recipe_name: str) -> list:
        recipes_query = "SELECT recipe_id FROM recipes WHERE recipe_name = ?;"
        return self.DB.get_recipes(recipes_query, recipe_name)

    def create_serve_query(self, recipe_name: str, meal_id: list) -> None:
        recipe_id = self.get_recipe_id(recipe_name)

        insert_query = {n: "INSERT INTO serve (meal_id, recipe_id) VALUES (?, ?);" for n in meal_id}
        serve_values = {n: [(n, recipe_id[0])] for n in meal_id}

        self.DB.add_to_tables(insert_query, serve_values)
        self.DB.commit_changes()
