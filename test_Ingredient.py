import pytest
from Ingredient import Ingredient

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