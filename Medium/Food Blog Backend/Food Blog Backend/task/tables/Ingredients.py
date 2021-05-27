from .Tables import Table


class Ingredients(Table):
    def __init__(self, table_name: str, db_name: str) -> None:
        super().__init__(table_name, db_name)
