from core.repository import Add, Update, Remove
from dominio.ingredient.ingredient import Ingredient


class IngredientRepository(Add, Update, Remove):
    def __init__(self, data: set[Ingredient]):
        super().__init__(data)

    def query(self, predicate, page=0, size=10):
        filtered_data = [item for item in self.data if predicate(item)]

        start_index = page * size
        end_index = start_index + size

        return filtered_data[start_index:end_index]


ingredient_repository = IngredientRepository(set())

__all__ = ["ingredient_repository"]
