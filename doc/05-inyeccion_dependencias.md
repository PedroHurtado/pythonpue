
# Opciones para inyectar repository en el servicio cumpliendo con el principio de inversión de dependencias (DI - SOLID)

## Código original
```python
def service(req: Request) -> Response:
    ingredient = Ingredient.ceate(uuid.uuid4(), req.name, req.cost)
    respository.add(ingredient)  # Usa un singleton global
    return Response(id=ingredient.id, name=ingredient.name, cost=ingredient.cost)
```

---

## 1️⃣ Inyección como argumento directo con `functools.partial`
```python
def service(req: Request, repository) -> Response:
    ingredient = Ingredient.ceate(uuid.uuid4(), req.name, req.cost)
    repository.add(ingredient)
    return Response(id=ingredient.id, name=ingredient.name, cost=ingredient.cost)

# Enlazar repository sin modificar el controlador
from functools import partial

service_with_repo = partial(service, repository=respository)

@bp.route("/ingredients", methods=["POST"])
def controller(body: Request):
    return service_with_repo(body), 201
```
✅ Ventajas:
- El `service` queda puro, sin dependencia global.
- Puedes usar mocks fácilmente en tests.
- El controlador no cambia.

---

## 2️⃣ Usar closure (factory de servicios)
```python
def make_service(repository):
    def service(req: Request) -> Response:
        ingredient = Ingredient.ceate(uuid.uuid4(), req.name, req.cost)
        repository.add(ingredient)
        return Response(id=ingredient.id, name=ingredient.name, cost=ingredient.cost)
    return service

service_with_repo = make_service(respository)

@bp.route("/ingredients", methods=["POST"])
def controller(body: Request):
    return service_with_repo(body), 201
```
✅ Ventajas:
- Muy flexible, puedes crear múltiples servicios con distintos repositorios.
- Ideal para testing.

---

## 3️⃣ Usar un objeto con `__call__`
```python
class IngredientService:
    def __init__(self, repository):
        self.repository = repository

    def __call__(self, req: Request) -> Response:
        ingredient = Ingredient.ceate(uuid.uuid4(), req.name, req.cost)
        self.repository.add(ingredient)
        return Response(id=ingredient.id, name=ingredient.name, cost=ingredient.cost)

service = IngredientService(respository)

@bp.route("/ingredients", methods=["POST"])
def controller(body: Request):
    return service(body), 201
```
✅ Ventajas:
- Inyección a través del constructor, compatible con frameworks de DI.
- Más extensible si luego agregas métodos adicionales o quieres heredar.

---

## 🚀 Conclusión
- Usa `partial` si quieres **mínimo cambio** y mantener el estilo funcional.
- Usa `make_service` si quieres **máxima ligereza y claridad**.
- Usa `__call__` si prefieres un diseño **orientado a objetos** y preparado para crecer.
