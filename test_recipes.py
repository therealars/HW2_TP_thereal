import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList
from DietaryRecipe import DietaryRecipe




def test_ingredient_creation():
    ingredient = Ingredient('Мука', 500, 'г')
    assert ingredient.name == 'Мука'
    assert ingredient.quantity == 500.0
    assert ingredient.unit == 'г'

def test_ingredient_quantity_must_be_positive():
    with pytest.raises(ValueError):
        Ingredient('Мука', 0, 'г')
    with pytest.raises(ValueError):
        Ingredient('Мука', -10, 'г')

def test_ingredient_quantity_converts_to_float():
    ingredient = Ingredient('Молоко', '250', 'мл')
    assert ingredient.quantity == 250.0

def test_ingredient_str():
    ingredient = Ingredient('Мука', 500, 'г')
    assert str(ingredient) == 'Мука: 500.0 г'

def test_ingredient_repr():
    ingredient = Ingredient('Мука', 500, 'г')
    assert repr(ingredient) == "Ingredient('Мука', 500.0, 'г')"

def test_ingredient_eq_same_name_and_unit_ignore_quantity():
    first = Ingredient('Мука', 500, 'г')
    second = Ingredient('Мука', 1000, 'г')
    assert first == second

def test_ingredient_eq_different_name():
    first = Ingredient('Мука', 500, 'г')
    second = Ingredient('Сахар', 500, 'г')
    assert first != second

def test_ingredient_eq_different_unit():
    first = Ingredient('Мука', 500, 'г')
    second = Ingredient('Мука', 500, 'кг')
    assert first != second




def test_recipe_creation():
    ingredients = [Ingredient('Мука', 500, 'г'), Ingredient('Яйцо', 2, 'шт')]
    recipe = Recipe('Блины', ingredients)
    assert recipe.title == 'Блины'
    assert recipe.ingredients == ingredients

def test_recipe_add_new_ingredient():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    egg = Ingredient('Яйцо', 2, 'шт')
    recipe.add_ingredient(egg)
    assert len(recipe.ingredients) == 2
    assert egg in recipe.ingredients

def test_recipe_add_existing_ingredient_sums_quantity():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    recipe.add_ingredient(Ingredient('Мука', 200, 'г'))
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == 'Мука'
    assert recipe.ingredients[0].quantity == 700.0
    assert recipe.ingredients[0].unit == 'г'

def test_recipe_add_same_name_different_unit_creates_new_ingredient():
    recipe = Recipe('Тесто', [Ingredient('Мука', 500, 'г')])
    recipe.add_ingredient(Ingredient('Мука', 1, 'кг'))
    assert len(recipe.ingredients) == 2

def test_recipe_scale_returns_new_recipe():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г'), Ingredient('Яйцо', 2, 'шт')])
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert scaled.title == 'Блины'
    assert scaled.ingredients[0].quantity == 1000.0
    assert scaled.ingredients[1].quantity == 4.0

def test_recipe_scale_does_not_change_original_recipe():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    scaled = recipe.scale(2)
    assert recipe.ingredients[0].quantity == 500.0
    assert scaled.ingredients[0].quantity == 1000.0

def test_recipe_scale_invalid_ratio():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-1)
    with pytest.raises(ValueError):
        recipe.scale('abc')

def test_recipe_len_returns_ingredients_count():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г'), Ingredient('Яйцо', 2, 'шт')])
    assert len(recipe) == 2

def test_recipe_str():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г'), Ingredient('Яйцо', 2, 'шт')])
    assert str(recipe) == 'Блины:\n - Мука: 500.0 г\n - Яйцо: 2.0 шт\n'






def test_shopping_list_add_recipe():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 2)
    result = shopping_list.get_List()
    assert len(result) == 1
    assert result[0].name == 'Мука'
    assert result[0].quantity == 1000.0
    assert result[0].unit == 'г'

def test_shopping_list_add_recipe_invalid_portions():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    shopping_list = ShoppingList()
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, 0)
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, -1)

def test_shopping_list_remove_recipe():
    pancakes = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    omelet = Recipe('Омлет', [Ingredient('Яйцо', 3, 'шт')])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(pancakes, 1)
    shopping_list.add_recipe(omelet, 1)
    shopping_list.remove_recipe('Блины')
    result = shopping_list.get_List()
    assert len(result) == 1
    assert result[0].name == 'Яйцо'

def test_shopping_list_remove_missing_recipe_does_nothing():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 1)
    shopping_list.remove_recipe('Несуществующий рецепт')
    result = shopping_list.get_List()
    assert len(result) == 1
    assert result[0].name == 'Мука'

def test_shopping_list_get_list_sums_same_ingredients_and_sorts_by_name():
    pancakes = Recipe('Блины', [Ingredient('Мука', 500, 'г'), Ingredient('Яйцо', 2, 'шт')])
    pie = Recipe('Пирог', [Ingredient('Мука', 300, 'г'), Ingredient('Сахар', 100, 'г')])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(pancakes, 1)
    shopping_list.add_recipe(pie, 1)
    result = shopping_list.get_List()
    assert [ingredient.name for ingredient in result] == ['Мука', 'Сахар', 'Яйцо']
    assert result[0].quantity == 800.0
    assert result[0].unit == 'г'

def test_shopping_list_add_operator_combines_lists():
    first_recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    second_recipe = Recipe('Омлет', [Ingredient('Яйцо', 3, 'шт')])
    first_list = ShoppingList()
    second_list = ShoppingList()
    first_list.add_recipe(first_recipe, 1)
    second_list.add_recipe(second_recipe, 1)
    combined = first_list + second_list
    result = combined.get_List()
    assert [ingredient.name for ingredient in result] == ['Мука', 'Яйцо']

def test_shopping_list_add_operator_does_not_change_original_lists():
    first_recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    second_recipe = Recipe('Омлет', [Ingredient('Яйцо', 3, 'шт')])
    first_list = ShoppingList()
    second_list = ShoppingList()
    first_list.add_recipe(first_recipe, 1)
    second_list.add_recipe(second_recipe, 1)
    combined = first_list + second_list
    assert len(first_list.get_List()) == 1
    assert len(second_list.get_List()) == 1
    assert len(combined.get_List()) == 2





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