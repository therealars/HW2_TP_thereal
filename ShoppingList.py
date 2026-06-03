from Ingredient import Ingredient
from Recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError('Количество порций должно быть положительным')
        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    
    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]
    
    def get_List(self):
        ingredient_dict = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in ingredient_dict:
                ingredient_dict[key] += ingredient.quantity
            else:
                ingredient_dict[key] = ingredient.quantity
        res = []
        for (name, unit), quantity in ingredient_dict.items():
            res.append(Ingredient(name, quantity, unit))
        res.sort(key=lambda ingredient: ingredient.name)
        return res
    def __add__(self, other: 'ShoppingList'):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list