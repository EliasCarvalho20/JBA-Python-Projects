from sqlite3 import connect, Error


class Database:
    def __init__(self) -> None:
        self.connection = None

    def make_connection(self, filename: str) -> None:
        self.connection = connect(filename)

    def create_tables(self, tables_to_create: dict) -> None:
        try:
            for values in tables_to_create.values():
                self.connection.execute(values)
        except Error as err:
            print(f"Error: {err}")

    def add_to_tables(self, data_query: dict, data: dict) -> None:
        try:
            for key, query in data_query.items():
                self.connection.executemany(query, data[key])
        except Error as err:
            print(f"Error: {err}")

    def get_meals(self, query: str) -> list:
        try:
            with self.connection:
                return self.connection.execute(query).fetchall()
        except Error as err:
            print(f"Error: {err}")

    def get_recipes(self, query: str, recipe_names: str) -> list:
        try:
            with self.connection:
                return self.connection.execute(query, (recipe_names,)).fetchone()
        except Error as err:
            print(f"Error: {err}")

    def commit_changes(self) -> None:
        self.connection.commit()

    def close_connection(self) -> None:
        self.connection.close()
