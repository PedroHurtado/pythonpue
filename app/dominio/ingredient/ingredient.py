from core.entitybase import EntityBase

class Ingredient(EntityBase):
    def __init__(self, id, name, cost):
        super().__init__(id)
        """
        no hacer acciones que afecten a puntos externos a la entidad:
            como por ejemplo registro de eventos
            no se distingir cuando me crean de cuando me
            recuperan de un sistema de persistenca

        """        
        self._name = name
        self._cost = cost    

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    def update(self, id, name, cost):
        # ingredients.update
        self._id = id
        self._name = name
        self._cost = cost

    @classmethod
    def ceate(cls, id, name, cost):
        # ingredient.creates
        return cls(id, name, cost)
