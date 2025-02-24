cookbook = {
  "Sandwich’s" : {
    "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
    "meal" : "lunch",
    "prep_time" : 10    
  },
  "Cake’s" : {
    "ingredients" : ["flour", "sugar", "eggs"],
    "meal" : "dessert",
    "prep_time" : 60
  },
  "Salad’s" : {
    "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
    "meal" : "lunch",
    "prep_time" : 15
  }
}

def recipe_names():
  if cookbook:
    print("Recipes in the cookbook:")
    for x in cookbook:
      print(f"- {x}")
    print("\n", end="")
  else:
    print("The book is empty.")
  
def recipe_details(name):
  if cookbook.get(name):
    print(f"{name}")
    print(f"Ingredients: {', '.join(cookbook[name]['ingredients'])}.")
    print(f"Meal type: {cookbook[name]['meal']}.")
    print(f"Preparation time: {cookbook[name]['prep_time']} min.")    
  else:
    print(f"{name} is not in the book.")
  
def del_recipe(name):
  if cookbook.get(name):
    cookbook.pop(name)
    print(f"{name} deleted.")
  else:
    print(f"{name} is not in the book.")

def add_recipe():
  name = input("Enter a name:\n")
  while name == "":
    name = input()
  enter = input("Enter ingredients:\n")
  ingredients = []
  while True:
    if enter != "":
      ingredients.append(enter)
    enter = input()
    if enter == "" and len(ingredients):
      break
  meal = input("Enter a meal type:\n")
  while meal == "":
    meal = input()
  prep_time = input("Enter a preparation time:\n")
  while not prep_time.isdigit() or int(prep_time) <= 0:
    prep_time = input("It must be a integer positive number.\n")
  prep_time = int(prep_time)
  cookbook.update({name: {"ingredients" : ingredients, "meal" : meal, "prep_time" : prep_time}})

if __name__ == "__main__":
  print("Welcome to the Python Cookbook !\n")
  while True:
    print("List of available option:\n")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    option = input("Please select an option:\n")
    while not option.isdigit() or (int(option) <= 0 or int(option) > 5):
      option = input("Please select a valid option.\n")
    option = int(option)
    if option == 1:
      add_recipe()
    elif option == 2:
      recipe_name = input("Please enter a recipe name to get its details:\n")
      del_recipe(recipe_name)
    elif option == 3:
      recipe_name = input("Please enter a recipe name to get its details:\n")
      recipe_details(recipe_name)
    elif option == 4:
      recipe_names()
    elif option == 5:
      print("Cookbook closed. Goodbye !")
      break