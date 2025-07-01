import copy
from core.entitybase import EntityBase



class Pizza(EntityBase):
    PROFIT = 1.2

    def __init__(self, id, name, description, url, ingredients):
        super().__init__(id)
        self._name = name
        self._description = description
        self._url = url
        self._ingredients = copy.deepcopy(ingredients)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def url(self):
        return self._url

    @property
    def ingredient(self):
        return copy.deepcopy(self._ingredients)

    @property
    def price(self):
        return sum(cost for _, cost in self._ingredients) * Pizza.PROFIT

    def add_ingredient(self, ingredient):
        # pizza.addingredient
        self._ingredients.add(ingredient)

    def remove_ingredient(self, ingredeint):
        # pizza.removeingredient
        self._ingredients.remove(ingredeint)

    @classmethod
    def create(cls, id, name, description, url, ingredients):
        # pizza.create
        return cls(id, name, description, url, ingredients)

    def update(self, name, description, url, ingredients):
        # pizza.update
        self._name = name
        self._description = description
        self._url = url
        self._ingredients = ingredients
