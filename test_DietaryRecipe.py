from Ingredient import Ingredient
from Recipe import Recipe
from DietaryRecipe import DietaryRecipe

def test_dietary_recipe_creation():
    recipe = DietaryRecipe('Овощной салат', 'Веганский', [Ingredient('Огурец', 2, 'шт')])
    assert recipe.title == 'Овощной салат'
    assert recipe.diet_type == 'Веганский'
    assert len(recipe.ingredients) == 1

def test_dietary_recipe_is_recipe_subclass():
    recipe = DietaryRecipe('Овощной салат', 'Веганский', [])
    assert isinstance(recipe, Recipe)

def test_dietary_recipe_scale_returns_dietary_recipe():
    recipe = DietaryRecipe('Овощной салат', 'Веганский', [Ingredient('Огурец', 2, 'шт')])
    scaled = recipe.scale(3)
    assert isinstance(scaled, DietaryRecipe)
    assert scaled is not recipe
    assert scaled.title == 'Овощной салат'
    assert scaled.diet_type == 'Веганский'
    assert scaled.ingredients[0].quantity == 6.0

def test_dietary_recipe_str():
    recipe = DietaryRecipe('Овощной салат', 'Веганский', [Ingredient('Огурец', 2, 'шт')])
    assert str(recipe) == '[Веганский] Овощной салат:\n - Огурец: 2.0 шт\n'