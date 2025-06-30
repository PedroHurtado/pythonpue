# Lambdas en Python: Guía Completa

## ¿Qué son las Lambdas?

Las **lambdas** son funciones anónimas pequeñas que pueden tener cualquier número de argumentos, pero solo pueden tener una expresión. Se definen usando la palabra clave `lambda` y son útiles cuando necesitas una función simple por un corto período de tiempo.

### Sintaxis Básica

```python
lambda argumentos: expresión
```

## Comparación: Lambdas vs Funciones Tradicionales

### Función Tradicional
```python
def cuadrado(x):
    return x ** 2

resultado = cuadrado(5)  # 25
```

### Lambda Equivalente
```python
cuadrado_lambda = lambda x: x ** 2
resultado = cuadrado_lambda(5)  # 25
```

## Características Principales

| Aspecto | Función Tradicional | Lambda |
|---------|-------------------|--------|
| **Sintaxis** | `def nombre():` | `lambda args:` |
| **Nombre** | Tiene nombre | Anónima |
| **Líneas de código** | Múltiples líneas | Una sola línea |
| **Complejidad** | Puede ser compleja | Solo expresiones simples |
| **Reutilización** | Fácil de reutilizar | Principalmente uso temporal |
| **Legibilidad** | Más legible para lógica compleja | Más concisa para operaciones simples |

## Ejemplos Prácticos

### 1. Operaciones Matemáticas Simples

```python
# Función tradicional
def suma(a, b):
    return a + b

# Lambda equivalente
suma_lambda = lambda a, b: a + b

print(suma(3, 4))        # 7
print(suma_lambda(3, 4)) # 7
```

### 2. Con Múltiples Argumentos

```python
# Lambda con múltiples argumentos
calcular = lambda x, y, z: (x + y) * z
print(calcular(2, 3, 4)) # 20
```

### 3. Sin Argumentos

```python
# Lambda sin argumentos
saludo = lambda: "¡Hola Mundo!"
print(saludo()) # ¡Hola Mundo!
```

## Uso Común con Funciones de Alto Nivel

Las lambdas brillan cuando se usan con funciones como `map()`, `filter()`, `sorted()`, etc.

### Con map()

```python
numeros = [1, 2, 3, 4, 5]

# Usando función tradicional
def duplicar(x):
    return x * 2

duplicados_func = list(map(duplicar, numeros))

# Usando lambda
duplicados_lambda = list(map(lambda x: x * 2, numeros))

print(duplicados_func)   # [2, 4, 6, 8, 10]
print(duplicados_lambda) # [2, 4, 6, 8, 10]
```

### Con filter()

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares con lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) # [2, 4, 6, 8, 10]

# Filtrar números mayores a 5
mayores_5 = list(filter(lambda x: x > 5, numeros))
print(mayores_5) # [6, 7, 8, 9, 10]
```

### Con sorted()

```python
estudiantes = [('Ana', 85), ('Luis', 90), ('María', 78), ('Carlos', 92)]

# Ordenar por nota (segundo elemento de la tupla)
por_nota = sorted(estudiantes, key=lambda x: x[1])
print(por_nota) # [('María', 78), ('Ana', 85), ('Luis', 90), ('Carlos', 92)]

# Ordenar por nombre (primer elemento)
por_nombre = sorted(estudiantes, key=lambda x: x[0])
print(por_nombre) # [('Ana', 85), ('Carlos', 92), ('Luis', 90), ('María', 78)]
```

## Ventajas de las Lambdas

### ✅ Pros
- **Concisas**: Código más corto para operaciones simples
- **Convenientes**: Perfectas para uso temporal con `map()`, `filter()`, etc.
- **Legibles**: Para operaciones simples, pueden ser más claras
- **Funcionales**: Facilitan el estilo de programación funcional

### ❌ Contras
- **Limitadas**: Solo una expresión, no declaraciones
- **Menos legibles**: Para lógica compleja pueden ser confusas
- **Difíciles de debuggear**: No tienen nombre, dificultan el debugging
- **No reutilizables**: Principalmente para uso único

## Cuándo Usar Cada Una

### Usa Lambdas cuando:
- Necesites una función simple de una línea
- La uses temporalmente con `map()`, `filter()`, `sorted()`
- La operación sea obvia y no requiera explicación
- Quieras código más conciso

```python
# Ideal para lambdas
numeros_ordenados = sorted(numeros, key=lambda x: abs(x))
```

### Usa Funciones Tradicionales cuando:
- La lógica sea compleja o requiera múltiples líneas
- Necesites reutilizar la función múltiples veces
- Requieras documentación o comentarios
- La función tenga un propósito específico y bien definido

```python
# Mejor como función tradicional
def validar_email(email):
    """Valida si un email tiene formato correcto"""
    if '@' not in email:
        return False
    partes = email.split('@')
    if len(partes) != 2:
        return False
    return '.' in partes[1]
```

## Ejemplos Avanzados

### Con reduce()

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Calcular el producto de todos los números
producto = reduce(lambda x, y: x * y, numeros)
print(producto) # 120
```

### En Comprensiones de Listas

```python
# Usando lambda dentro de una comprensión
operacion = lambda x: x**2 + 2*x + 1
resultados = [operacion(i) for i in range(5)]
print(resultados) # [1, 4, 9, 16, 25]
```

### Con Diccionarios

```python
productos = [
    {'nombre': 'Laptop', 'precio': 1000},
    {'nombre': 'Mouse', 'precio': 25},
    {'nombre': 'Teclado', 'precio': 75}
]

# Ordenar productos por precio
por_precio = sorted(productos, key=lambda x: x['precio'])
print(por_precio)
```

## Consejos y Mejores Prácticas

1. **Mantén las lambdas simples**: Si necesitas más de una línea, usa una función normal
2. **Usa nombres descriptivos**: Aunque sean anónimas, los parámetros deben ser claros
3. **No abuses de ellas**: No toda función pequeña debe ser lambda
4. **Considera la legibilidad**: A veces una función nombrada es más clara

```python
# ✅ Bueno: Simple y claro
numeros_pares = filter(lambda x: x % 2 == 0, numeros)

# ❌ Malo: Demasiado complejo para lambda
# Mejor usar función normal
complejo = lambda x: x**2 + 3*x - 2 if x > 0 else abs(x) * 2 + 1
```

## Conclusión

Las lambdas son una herramienta poderosa en Python que complementa a las funciones tradicionales. Úsalas para operaciones simples y temporales, especialmente con funciones de alto nivel como `map()`, `filter()`, y `sorted()`. Para lógica compleja, reutilización frecuente, o cuando necesites claridad en el código, las funciones tradicionales siguen siendo la mejor opción.

La clave está en elegir la herramienta correcta para cada situación: lambdas para simplicidad y concisión, funciones tradicionales para complejidad y reutilización.