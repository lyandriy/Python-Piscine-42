from book import Book
from recipe import Recipe

if __name__ == "__main__":
    
    book = Book("Libro de Recetas")
    
    recipe1 = Recipe("Tortilla Española", 3, 30, ["4 huevos", "3 patatas medianas", "1 cebolla, aceite de oliva", "sal"], "Un clásico de la gastronomía española, la tortilla de patatas es una mezcla deliciosa de huevos y patatas doradas", "lunch")
    recipe2 = Recipe("Ensalada Caprese", 1, 10, ["2 tomates", "200 g de mozzarella fresca", "hojas de albahaca", "aceite de oliva", "sal", "pimienta", "vinagre balsámico"], "Una ensalada ligera y refrescante, ideal para empezar una comida con un toque mediterráneo", "starter")
    recipe3 = Recipe("Risotto de Champiñones", 4, 40, ["200 g de arroz arborio", "500 ml de caldo de verduras", "150 g de champiñones", "1 cebolla", "50 g de parmesano rallado", "50 ml de vino blanco, mantequilla", "aceite de oliva", "sal", "pimienta"], "", "lunch")
    recipe4 = Recipe("Tiramisú", 4, -30, ["250 g de mascarpone", "2 huevos", "50 g de azúcar", "200 ml de café", "100 g de bizcochos de soletilla", "cacao en polvo"], "Un postre italiano cremoso y lleno de sabor, con capas de mascarpone y bizcocho empapado en café.", "dessert")
    
    book.add_recipe(recipe1)
    book.add_recipe(recipe2)
    book.add_recipe(recipe3)
    book.add_recipe(recipe4)
    
    book.get_recipe_by_name("Risotto de Champiñones")
    print(book.get_recipes_by_types("starter"))