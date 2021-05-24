from sqlite3 import connect, Error


class DBConnection:
    def __init__(self, db_name: str) -> None:
        self.connection = None
        self.cursor = None
        self.db_name = db_name

    def create_connection(self) -> None:
        self.connection = connect(self.db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str) -> None:
        try:
            with self.connection:
                self.cursor.execute(query)
        except Error as err:
            print(f"Error: {err}")

    def execute_many(self, query: str, data: list) -> None:
        try:
            with self.connection:
                self.cursor.executemany(query, data)
        except Error as err:
            print(f"Error: {err}")

    def select_one(self, query: str, param: str) -> None:
        try:
            with self.connection:
                self.cursor.execute(query, (param,))
        except Error as err:
            print(f"Error: {err}")

    def select_all(self, query: str) -> None:
        try:
            with self.connection:
                self.cursor.execute(query)
        except Error as err:
            print(f"Error: {err}")
