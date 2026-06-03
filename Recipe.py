from Ingredient import Ingredient

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient):
        if ingredient in self.ingredients and ingredient.unit == self.ingredients[self.ingredients.index(ingredient)].unit:
            self.ingredients[self.ingredients.index(ingredient)].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        if (not isinstance(ratio, int) and not isinstance(ratio, float)) or ratio <= 0:
            return False
        return True
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError('Коэффициент должен быть положительным числом')
        new_ingredients = []
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            new_ingredients.append(new_ingredient)
        return Recipe(self.title, new_ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        res = f'{self.title}:\n'
        for ingredient in self.ingredients:
            res += f' - {ingredient}\n'
        return res