from uuid import uuid4
class Ingredient:
    def __init__(self,id:uuid4,name:str,cost:float):
        self._id= id
        self._name = name
        self._cost = cost
    def __eq__(self, value):
        if not isinstance(value,Ingredient):
            return False
        return self._id == value._id
    def __hash__(self):
        return hash(self._id)

tomate = Ingredient(1,"Tomate",2.0)
tomate1 = Ingredient(1,"Tomate",2.0)

ingredients = set()
ingredients.add(tomate)
ingredients.add(tomate1)


print(tomate1==tomate) #false
print(len(ingredients))

tomate=1
tomate1=1

numbers = set()
numbers.add(tomate)
numbers.add(tomate1)
print(tomate==tomate1) #true
print(len(numbers))