from app.core.data import Data
from app.core.entitybase import EntityBase
from app.core.notfoundexception import NotFoundException

class Add(Data):
    def add(self,entity:EntityBase):
        self.data.add(entity)        
class Get(Data):
    def find(self,id, message="La entidad no existe"):
         entity = next((e for e in self.data if e.id == id), None)       
         if entity is None:
            raise NotFoundException(message)
         return entity
class Update(Get):
    def update(self,entity:EntityBase):        
        self.data.remove(entity)
        self.data.add(entity)
class Remove(Get):
    def remove(self,entity):
        self.data.remove(entity)


        