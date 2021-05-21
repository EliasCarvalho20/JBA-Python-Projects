import sys
from models.food_blog import FoodBlog


class Menu:
    def __init__(self) -> None:
        self.FOOD_BLOG = FoodBlog()

    def execute(self) -> None:
        try:
            args = sys.argv[1]
            # args = "food_blog.db"

            self.FOOD_BLOG = FoodBlog()
            self.FOOD_BLOG.make_connection(args)
            self.FOOD_BLOG.execute()

            self.show_menu()

        except IndexError:
            self.exit_program()

    def show_menu(self) -> None:
        print("Pass the empty recipe name to exit.")

        while (recipe_name := input("Recipe name: ")) != "":
            recipe_description = input("Recipe description: ")

            self.FOOD_BLOG.set_recipes(recipe_name, recipe_description)

        self.FOOD_BLOG.create_recipes_query()

    @staticmethod
    def exit_program() -> None:
        sys.exit()


if __name__ == "__main__":
    menu = Menu()
    menu.execute()
