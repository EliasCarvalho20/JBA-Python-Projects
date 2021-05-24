import sys
import argparse

from data.food_data import DATA
from tables.Ingredients import Ingredients
from tables.Meals import Meals
from tables.Measure import Measure
from tables.Recipes import Recipes
from tables.Serve import Serve
from tables.Quantity import Quantity


class Menu:
    def __init__(self, db_name: str) -> None:
        self.tables = None
        self.ingredients_table = Ingredients(db_name)
        self.meals_table = Meals(db_name)
        self.measure_table = Measure(db_name)
        self.recipes_table = Recipes(db_name)
        self.serve_table = Serve(db_name)
        self.quantity_table = Quantity(db_name)
        self.meals_list = []

    def execute(self) -> None:
        self.tables = [
            self.meals_table, self.ingredients_table, self.measure_table,
            self.recipes_table, self.serve_table, self.quantity_table
        ]

        self.create_and_populate_tables()
        self.show_menu()

    def create_and_populate_tables(self) -> None:
        for index, key in enumerate(DATA.keys()):
            self.tables[index].create_table()
            self.tables[index].populate_table(DATA[key])

        for table in self.tables[3:]:
            table.create_table()

    def show_menu(self) -> None:
        print("Pass the empty recipe name to exit.")

        while True:
            recipe_name = input("Recipe name: ")

            if recipe_name == "":
                for table in self.tables:
                    table.db.connection.close()

                exit_program("Bye!")

            recipe_description = input("Recipe description: ")
            recipe_id = self.recipes_table.populate(recipe_name, recipe_description)

            self.show_options(recipe_id)

    def show_options(self, recipe_id: int) -> None:
        if not self.meals_list:
            self.meals_list = self.meals_table.get_all_meals()

        print(*[f"{meal[0]}) {meal[1]}" for meal in self.meals_list], sep=" ")
        meal_id = [int(n) for n in input("Enter proposed meals separated by a space: ").split()]

        self.serve_table.populate(meal_id, recipe_id)

        while len(arguments := input("Input quantity of ingredient <press enter to stop>: ").split()) != 0:
            quantity, *rest = arguments

            measure, ingredients = self.check_options(rest)
            if len(measure) > 1 or len(ingredients) > 1:
                print("The measure is not conclusive!")
                continue

            self.quantity_table.populate(int(quantity), measure[0], ingredients[0], recipe_id)

    @staticmethod
    def check_options(params: list) -> tuple:
        if len(params) == 2:
            measure, ingredients = params[0], params[1]
        else:
            measure, ingredients = "", params[0]

        msr_quantity = [""]

        if measure:
            msr_quantity = [msr[0] for msr in DATA["measures"] if msr[0].startswith(measure)]

        ing_quantity = [ing[0] for ing in DATA["ingredients"] if ing[0].find(ingredients) != -1]

        return msr_quantity, ing_quantity


def cli_arguments() -> str:
    parser = argparse.ArgumentParser(description="A simple program that creates and populates a recipe database")
    parser.add_argument("db_name", type=str, help="The database name")
    return parser.parse_args().db_name


def exit_program(message: str) -> None:
    sys.exit(message)


if __name__ == "__main__":
    # db_name = self.cli_arguments()
    db_name = "food_blog.db"

    if not db_name:
        exit_program("No database name provided")

    menu = Menu(db_name)
    menu.execute()
