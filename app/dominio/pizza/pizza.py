import copy

class Pizza:
    def __init__(self,id,name,description,url,ingredients):
        self._id= id,
        self._name = name
        self._description = description
        self._url = url
        self._ingredients = copy.deepcopy(ingredients)
    @property
    def id(self):
        return self._id
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
        result = 0
        for ingredient in self._ingredients:
            result+=ingredient.cost
        return result * 1.2            
    def add_ingredient(self,ingredient):
        #pizza.addingredient
        self._ingredients.add(ingredient)
    def remove_ingredient(self,ingredeint):
        #pizza.removeingredient
        self._ingredients.remove(ingredeint)
    @classmethod
    def create(cls,id,name,description,url,ingredients):
        #pizza.create
        return cls(id,name,description,url,ingredients)
    def update(self,name,description,url,ingredients):
        #pizza.update
        self._name = name
        self._description = description
        self._url = url
        self._ingredients = ingredients