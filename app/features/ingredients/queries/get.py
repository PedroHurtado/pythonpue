import uuid
from app.dominio.ingredient.ingredient import Ingredient
from app.core.custombasemodel import CustomBaseModel
from flask import Blueprint,jsonify
from flask_pydantic import validate
from app.infraestructure.ingredients.ingredientsrepository import (
    ingredient_repository as respository,
)

bp = Blueprint("ingredient_get", __name__)

class Response(CustomBaseModel):
    id: uuid.UUID
    name: str
    cost: float


class Service:
    def __init__(self, repository):
        self._repository = repository
    def __call__(self, id: uuid.UUID) -> Response:
        ingredient:Ingredient = respository.find(id)
        return Response(id=ingredient.id, name=ingredient.name, cost=ingredient.cost)


service = Service(respository)

@bp.route("/ingredients/<uuid:id>")
@validate()
def controller(id:uuid.UUID):
    return service(id)
