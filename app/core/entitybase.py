
"""
1. crear una clase abstracta
2. llevar el id a la entity base(agregarlo al constructor y agregarlo property)
3. reemplazar el __eq__ y el __hash__
4. heredar en ingredeint y en pizza
    super().__init(id)
"""

from abc import ABC

class EntityBase(ABC):
    def __init__(self, id):
        self._id = id
    @property
    def id(self):
        return self._id
    def __eq__(self, value):
        if not isinstance(value, EntityBase):
            return False
        return self._id == value._id
    def __hash__(self):
        return hash(self._id)