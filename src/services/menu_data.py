from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        menu_data = pd.read_csv(source_path)
        unique_dishes = menu_data["dish"].unique()

        for dish in unique_dishes:
            df = menu_data.loc[menu_data["dish"] == dish]
            price = df["price"].unique()[0]

            new_dish = Dish(dish, price)

            ingredients = df[["ingredient", "recipe_amount"]].values.tolist()

            for ingredient, amount in ingredients:
                new_ingredient = Ingredient(ingredient)
                new_dish.add_ingredient_dependency(new_ingredient, amount)

            self.dishes.add(new_dish)
