import sys
from models.food_blog import FoodBlog


class Menu:
    def __init__(self) -> None:
        self.FOOD_BLOG = FoodBlog()
        self.meals_list = None

    def execute(self, filename: str) -> None:
        self.FOOD_BLOG.DB.make_connection(filename)
        self.FOOD_BLOG.execute()

        self.show_menu()

    def show_menu(self) -> None:
        print("Pass the empty recipe name to exit.")

        while True:
            recipe_name = input("Recipe name: ")

            if recipe_name == "":
                self.FOOD_BLOG.DB.close_connection()
                exit_program()

            recipe_description = input("Recipe description: ")

            self.FOOD_BLOG.set_recipes(recipe_name, recipe_description)
            self.FOOD_BLOG.create_recipes_query()

            print()

            if not self.meals_list:
                self.meals_list = self.FOOD_BLOG.get_meals()

            print(*[f"{meal[0]}) {meal[1]}" for meal in self.meals_list], sep=" ")

            meal_id = [int(n) for n in input("When the dish can be served: \n").split()]
            self.FOOD_BLOG.create_serve_query(recipe_name, meal_id)


def exit_program() -> None:
    print("Bye!")
    sys.exit()


if __name__ == "__main__":
    try:
        # args = sys.argv[1]
        args = "food_blog.db"

        menu = Menu()
        menu.execute(args)
    except IndexError:
        exit_program()
