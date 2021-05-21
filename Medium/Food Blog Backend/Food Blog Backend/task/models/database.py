from sqlite3 import connect, Error


class Database:
    def __init__(self, filename: str) -> None:
        self.FILE_NAME = filename
        self.connection = None

    def create_connection(self) -> None:
        self.connection = connect(self.FILE_NAME)

    def create_tables(self, tables_to_create: dict) -> None:
        try:
            for values in tables_to_create.values():
                with self.connection:
                    self.connection.execute(values)
        except Error as err:
            print(f"Error: {err}")

    def add_to_tables(self, data: dict, data_query: dict) -> None:
        try:
            for key, query in data_query.items():
                for values in data[key]:
                    with self.connection:
                        self.connection.execute(query, (values,))
        except Error as err:
            print(f"Error: {err}")

    def add_values_to_recipes(self, data: dict, data_query: dict) -> None:
        try:
            for key, query in data_query.items():
                temp = tuple(data[key])

                with self.connection:
                    self.connection.executemany(query, (temp,))
        except Error as err:
            print(f"Error: {err}")

    def commit_changes(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
