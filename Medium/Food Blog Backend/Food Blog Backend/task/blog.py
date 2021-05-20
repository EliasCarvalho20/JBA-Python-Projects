import sys
from models.food_blog import FoodBlog

if __name__ == "__main__":
    args = sys.argv[1]
    food_blog = FoodBlog()
    food_blog.make_connection(args)
    food_blog.execute()
