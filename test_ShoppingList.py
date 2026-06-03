import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList

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