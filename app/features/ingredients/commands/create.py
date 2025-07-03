import uuid
from app.dominio.ingredient.ingredient import Ingredient
from flask import Blueprint
from app.infraestructure.ingredients.ingredientsrepository import ingredient_repository as respository

bp = Blueprint('ingredient_create', __name__)

class Request:
    name:str
    cost:float

class Response:
    id:uuid
    name:str
    cost:float

def service(req:Request)->Response:
    ingredient = Ingredient.ceate(
        uuid.uuid4(),
        req.name,
        req.cost
    )
    respository.add(ingredient)    
    return Response(ingredient.id, ingredient.name,ingredient.cost)

@bp.route("/ingredients")
def controller(body:Request):
    return service(body),201