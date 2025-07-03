# API REST - Pizza Service

## Descripción General

Esta API REST permite gestionar un sistema de pizzas e ingredientes. Proporciona operaciones CRUD completas para ambos recursos siguiendo las mejores prácticas de diseño de APIs RESTful.

## Configuración del Servidor

- **URL Base**: `http://localhost:5000` o `127.0.0.1:5000`
- **Protocolo**: HTTP
- **Formato**: JSON

## Modelos de Datos

### Pizza
```json
{
  "id": "integer",
  "name": "string",
  "description": "string", 
  "url": "string",
  "price": "number (calculado: sum(ingredient.cost) * 1.2)",
  "ingredients": [
    {
      "id": "integer",
      "name": "string",
      "cost": "number"
    }
  ]
}
```

### Ingredient
```json
{
  "id": "integer",
  "name": "string",
  "cost": "number"
}
```

## Reglas de Diseño de URLs

### 1. Pluralización de Recursos
- ✅ **Correcto**: `/pizzas`
- ❌ **Incorrecto**: `/pizza`

### 2. No Expresar Acciones en URLs
- ✅ **Correcto**: `POST /pizzas` (crear)
- ❌ **Incorrecto**: `/pizzas/add`

**Mapeo de Verbos HTTP:**
- `POST` → Crear
- `GET` → Leer
- `PUT/PATCH` → Modificar
- `DELETE` → Eliminar

### 3. No Especificar Formato en URLs
- ✅ **Correcto**: `/pizzas` con headers `Accept: application/json`
- ❌ **Incorrecto**: `/pizzas.json`

**Uso de Headers:**
- `Accept: application/json` - Formato esperado en respuesta
- `Content-Type: application/json` - Formato del cuerpo de la petición

### 4. Versionado
- `v1`: `/v1/pizzas`
- `v2`: `/v2/pizzas`

## Endpoints

### Pizzas

#### 1. Crear Pizza
```http
POST /pizzas
Content-Type: application/json
Accept: application/json

{
  "name": "Margherita",
  "description": "Pizza clásica con tomate, mozzarella y albahaca",
  "url": "https://example.com/margherita.jpg",
  "ingredients": [1, 2, 3]
}
```

**Respuesta Exitosa:**
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "Margherita",
  "description": "Pizza clásica con tomate, mozzarella y albahaca",
  "url": "https://example.com/margherita.jpg",
  "price": 12.50,
  "ingredients": [...]
}
```

#### 2. Obtener Todas las Pizzas
```http
GET /pizzas
Accept: application/json
```

**Parámetros de Query String:**
- `name`: Filtrar por nombre
- `page`: Número de página (default: 0)
- `size`: Tamaño de página (default: 25)

**Ejemplo:** `GET /pizzas?name=margherita&page=0&size=10`

**Respuesta Exitosa:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": 1,
    "name": "Margherita",
    "description": "Pizza clásica...",
    "url": "https://example.com/margherita.jpg",
    "price": 12.50,
    "ingredients": [...]
  }
]
```

#### 3. Obtener Pizza por ID
```http
GET /pizzas/{id}
Accept: application/json
```

**Respuesta Exitosa:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Margherita",
  "description": "Pizza clásica...",
  "url": "https://example.com/margherita.jpg",
  "price": 12.50,
  "ingredients": [...]
}
```

#### 4. Actualizar Pizza
```http
PUT /pizzas/{id}
Content-Type: application/json
Accept: application/json

{
  "name": "Margherita Premium",
  "description": "Pizza clásica con ingredientes premium",
  "url": "https://example.com/margherita-premium.jpg",
  "ingredients": [1, 2, 3, 4]
}
```

**Respuesta Exitosa:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Margherita Premium",
  "description": "Pizza clásica con ingredientes premium",
  "url": "https://example.com/margherita-premium.jpg",
  "price": 15.60,
  "ingredients": [...]
}
```

**Respuesta Alternativa (Sin Cuerpo):**
```http
HTTP/1.1 204 No Content
```

#### 5. Eliminar Pizza
```http
DELETE /pizzas/{id}
```

**Respuesta Exitosa:**
```http
HTTP/1.1 204 No Content
```

### Ingredients

#### 1. Crear Ingrediente
```http
POST /ingredients
Content-Type: application/json
Accept: application/json

{
  "name": "Mozzarella",
  "cost": 3.50
}
```

#### 2. Obtener Todos los Ingredientes
```http
GET /ingredients
Accept: application/json
```

#### 3. Obtener Ingrediente por ID
```http
GET /ingredients/{id}
Accept: application/json
```

#### 4. Actualizar Ingrediente
```http
PUT /ingredients/{id}
Content-Type: application/json
Accept: application/json

{
  "name": "Mozzarella Premium",
  "cost": 4.00
}
```

#### 5. Eliminar Ingrediente
```http
DELETE /ingredients/{id}
```

## Códigos de Estado HTTP

### Respuestas Exitosas
- `200 OK` - Petición exitosa con contenido
- `201 Created` - Recurso creado exitosamente
- `204 No Content` - Petición exitosa sin contenido

### Errores del Cliente (4xx)
- `400 Bad Request` - Error de validación en los datos
- `401 Unauthorized` - No autenticado
- `403 Forbidden` - No autorizado
- `404 Not Found` - Recurso no encontrado
- `405 Method Not Allowed` - Método HTTP no permitido
- `409 Conflict` - Conflicto con el estado actual del recurso
- `415 Unsupported Media Type` - Tipo de contenido no soportado

### Errores del Servidor (5xx)
- `500 Internal Server Error` - Error interno del servidor

## Ejemplos de Respuestas de Error

### Error de Validación
```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "Validation Error",
  "message": "El nombre es requerido",
  "details": {
    "field": "name",
    "code": "required"
  }
}
```

### Recurso No Encontrado
```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "Not Found",
  "message": "Pizza con ID 999 no encontrada"
}
```

## Notas Adicionales

### Cálculo de Precios
El precio de cada pizza se calcula automáticamente usando la fórmula:
```
price = sum(ingredient.cost) * 1.2
```

### Formato de Datos
- Todos los intercambios de datos se realizan en formato JSON
- Las fechas deben enviarse en formato ISO 8601
- Los números decimales usan punto como separador

### Paginación
Para endpoints que retornan colecciones, se puede usar paginación:
- `page`: Número de página (inicia en 0)
- `size`: Cantidad de elementos por página (máximo 100)

### Filtros
Los endpoints de colección soportan filtros básicos a través de query parameters que coinciden con los nombres de los campos del modelo.