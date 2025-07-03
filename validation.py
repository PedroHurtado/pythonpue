from typing import Optional, List

class RequestQuery:
    id:int    
    name:Optional[str]=None
    cost:float
class RequestBody:
    ingredients:dict[str,int]

print(RequestQuery.__annotations__)
print(RequestBody.__annotations__)