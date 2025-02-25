from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        try:
            if not isinstance(name, str):
                raise TypeError("Invalid name type.")
            self.name = str(name)
            self.last_update = datetime.now()
            self.creation_date = datetime.now()
            self.recipes_list = {
                "starter": [],
                "lunch": [],
                "dessert": [],                
            }
        except (ValueError, TypeError) as e:
            print(f"ERROR: {e}")
            
    def get_recipe_by_name(self, name):
        count = 0
        for type in self.recipes_list.values():
            for recipe in type:
                if recipe.name == name:
                    print(recipe)
                    count += 1
        if count == 0:
            print(f"No {name}, recipe")

    def get_recipes_by_types(self, recipe_type):
        recipe_list = []
        recipe_types = self.recipes_list.get(recipe_type)
        if recipe_types is None:
            print("Invalid recipe type.")
        else:
            for x in recipe_types:
                recipe_list.append(x.name)
            if not recipe_list:
                print("No recipes found for this type.")
        return recipe_list

    def add_recipe(self, recipe):
        try:
            if isinstance(recipe, Recipe):
                if recipe.recipe_type in self.recipes_list:
                    self.recipes_list[recipe.recipe_type].append(recipe)
                    self.last_update = datetime.now()
                else:
                    print("Invalid type of recipe.")
            else:
                print("Invalid argument recipe.")
        except Exception as e:
            print(f"Error adding recipe: {e}")
            