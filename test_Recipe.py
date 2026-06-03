import pytest
from Ingredient import Ingredient
from Recipe import Recipe

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