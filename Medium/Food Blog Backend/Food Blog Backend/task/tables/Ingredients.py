from .Tables import Table


class Ingredients(Table):
    def __init__(self, db_name: str) -> None:
        super().__init__(db_name)
        self.table_name = "ingredient"
