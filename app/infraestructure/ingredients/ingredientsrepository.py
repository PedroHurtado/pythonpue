from core.repository import Add,Update,Remove
from dominio.ingredient.ingredient import Ingredient
class IngredientRepository(Add,Update,Remove):
    def __init__(self, data:set[Ingredient]):
        super().__init__(data)
    def find_by_name(self,name:str):
        pass