class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if self._validate(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
        
    def _validate(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not isinstance(name, str):
            print("Invalid name type.")
            return False
        if not isinstance(cooking_lvl, int):
            print("Invalid cooking level type.")
            return False
        if  not (1 <= cooking_lvl <= 5):
            print("Cooking level range mast be from 1 to 5.")
            return False
        if not isinstance(cooking_time, int):
            print("Invalid cooking time type.")
            return False
        if cooking_time < 0:
            print("Cooking time mast be a positive number.")
            return False
        if not isinstance(ingredients, list):
            print("Invalid ingredients type")
            return False
        if not ingredients:
            print("Ingredients list is empty.")
            return False
        if not isinstance(description, str):
            print("Invalid description type.")
            return False
        if not isinstance(recipe_type, str):
            print("Invalid recipe type.")
            return False
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("Invalid recipe type.")
            return False
        return True
            
    def __str__(self):
        txt = f"Recipe name: {self.name}\n"
        txt += f"Cooking level: {self.cooking_lvl}\n"
        txt += f"Cooking time: {self.cooking_time}\n"
        txt += f"Ingredients: {', '.join(self.ingredients)}\n"
        txt += f"Description: {self.description}\n"
        txt += f"Recipe type: {self.recipe_type}\n"        
        return txt