import uuid
from app.dominio.ingredient.ingredient import Ingredient
from app.core.custombasemodel import CustomBaseModel
from flask import Blueprint
from pydantic import StringConstraints
from typing import Annotated
from flask_pydantic import validate
from app.infraestructure.ingredients.ingredientsrepository import (
    ingredient_repository as respository,
)

bp = Blueprint("ingredient_create", __name__)


class Request(CustomBaseModel):
    name: Annotated[str, StringConstraints(min_length=1)]
    cost: float


class Response(CustomBaseModel):
    id: uuid
    name: str
    cost: float


class Service:
    def __init__(self, repository):
        self._repository = repository
    def __call__(self, req: Request) -> Response:
        ingredient = Ingredient.create(uuid.uuid4(), req.name, req.cost)
        self._repository.add(ingredient)
        return Response(id=ingredient.id, name=ingredient.name, cost=ingredient.cost)


service = Service(respository)

@bp.route("/ingredients", methods=["POST"])
@validate()
def controller(body: Request):
    return service(body), 201
