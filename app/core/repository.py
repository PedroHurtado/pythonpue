from data import Data
class Add(Data):
    def add(self,entity):
        pass        
class Get(Data):
    def find(self,id):
        pass
class Update(Get):
    def update(self,entity):
        pass
class Remove(Get):
    def remove(self,entity):
        pass
        