from models.ingredient import Ingredient
from models.dish import Dish
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.set_formatted_dishes(source_path)

    def set_formatted_dishes(self, source_path):
        formatted_dishes = {}
        with open(source_path, "r") as file:
            data = csv.DictReader(file)

            for line in data:
                dish_name = line["dish"]
                price = float(line["price"])
                ingredient = Ingredient(line["ingredient"])
                amount = int(line["recipe_amount"])

                if dish_name not in formatted_dishes:
                    formatted_dishes[dish_name] = Dish(dish_name, price)

                formatted_dishes[dish_name].add_ingredient_dependency(
                    ingredient,
                    amount
                )

        self.dishes = formatted_dishes.values()
