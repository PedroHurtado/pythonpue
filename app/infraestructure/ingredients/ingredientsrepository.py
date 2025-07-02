from core.repository import Add, Update, Remove
from dominio.ingredient.ingredient import Ingredient


class IngredientRepository(Add, Update, Remove):
    def __init__(self, data: set[Ingredient]):
        super().__init__(data)
    def query(predicate,page=0,size=10):
        """
        sobre el data aplicar un filter y obtener 
        solo pagina indicada y el numero de elementos por página
        """
        pass
    
ingredient_repository =IngredientRepository(set())

__all__ = ['ingredient_repository']
