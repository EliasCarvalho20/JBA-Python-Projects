from sqlite3 import connect, Connection


class Database:
    def __init__(self, filename: str) -> None:
        self.FILE_NAME = filename
        self.connection = None

    def create_connection(self) -> None:
        self.connection = connect(self.FILE_NAME)

    def create_tables(self, tables_to_create: dict) -> None:
        for values in tables_to_create.values():
            with self.connection:
                self.connection.execute(values)

    def add_to_tables(self, data: dict, data_query: dict) -> None:
        for key, query in data_query.items():
            for values in data[key]:
                with self.connection:
                    self.connection.execute(query, (values,))

    def commit_changes(self):
        self.connection.commit()
