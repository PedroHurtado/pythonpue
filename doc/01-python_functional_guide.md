# Guía de Programación Funcional en Python

## Introducción

La programación funcional es un paradigma que trata la computación como la evaluación de funciones matemáticas. En Python, aunque no es un lenguaje puramente funcional, podemos aplicar muchos conceptos funcionales que nos ayudan a escribir código más limpio, legible y mantenible.

Esta guía se centra en cinco funciones fundamentales: `filter()`, `map()`, `reduce()`, `sorted()` y técnicas para implementar `find()`.

## Conceptos Básicos

### Funciones de Primera Clase
En Python, las funciones son objetos de primera clase, lo que significa que pueden:
- Asignarse a variables
- Pasarse como argumentos
- Retornarse desde otras funciones
- Almacenarse en estructuras de datos

### Funciones Lambda
Las funciones lambda son funciones anónimas que se definen en una sola línea:

```python
# Función tradicional
def cuadrado(x):
    return x ** 2

# Función lambda equivalente
cuadrado_lambda = lambda x: x ** 2
```

## 1. Filter - Filtrar Elementos

La función `filter()` crea un iterador con los elementos que cumplen una condición específica.

### Sintaxis
```python
filter(función, iterable)
```

### Ejemplos Básicos

```python
# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Filtrar palabras con más de 5 caracteres
palabras = ["python", "java", "javascript", "go", "rust", "typescript"]
palabras_largas = list(filter(lambda palabra: len(palabra) > 5, palabras))
print(palabras_largas)  # ['python', 'javascript', 'typescript']
```

### Ejemplos Avanzados

```python
# Filtrar diccionarios
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 19, "nota": 7.2},
    {"nombre": "María", "edad": 21, "nota": 9.1},
    {"nombre": "Carlos", "edad": 18, "nota": 6.8}
]

# Estudiantes aprobados (nota >= 7.0)
aprobados = list(filter(lambda est: est["nota"] >= 7.0, estudiantes))

# Estudiantes mayores de 19 años
mayores = list(filter(lambda est: est["edad"] > 19, estudiantes))
```

### Uso con Funciones Definidas

```python
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = range(2, 50)
primos = list(filter(es_primo, numeros))
print(primos)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

## 2. Map - Transformar Elementos

La función `map()` aplica una función a cada elemento de un iterable.

### Sintaxis
```python
map(función, iterable)
```

### Ejemplos Básicos

```python
# Elevar al cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# Convertir a mayúsculas
nombres = ["ana", "luis", "maría", "carlos"]
nombres_mayus = list(map(str.upper, nombres))
print(nombres_mayus)  # ['ANA', 'LUIS', 'MARÍA', 'CARLOS']
```

### Múltiples Iterables

```python
# Sumar elementos de dos listas
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]
sumas = list(map(lambda x, y: x + y, lista1, lista2))
print(sumas)  # [11, 22, 33, 44]

# Calcular potencias
bases = [2, 3, 4, 5]
exponentes = [3, 2, 2, 3]
potencias = list(map(lambda b, e: b ** e, bases, exponentes))
print(potencias)  # [8, 9, 16, 125]
```

### Ejemplos Avanzados

```python
# Transformar diccionarios
productos = [
    {"nombre": "Laptop", "precio": 1000},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 75}
]

# Aplicar descuento del 10%
con_descuento = list(map(
    lambda p: {**p, "precio_descuento": p["precio"] * 0.9},
    productos
))

# Formatear strings
def formatear_producto(producto):
    return f"{producto['nombre']}: ${producto['precio']:.2f}"

productos_formateados = list(map(formatear_producto, productos))
```

## 3. Reduce - Reducir a un Solo Valor

La función `reduce()` aplica una función de dos argumentos de manera acumulativa a los elementos de un iterable.

### Importación y Sintaxis
```python
from functools import reduce

reduce(función, iterable[, inicial])
```

### Ejemplos Básicos

```python
from functools import reduce

# Suma de todos los elementos
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 15

# Producto de todos los elementos
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # 120

# Encontrar el máximo
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(maximo)  # 5
```

### Ejemplos Avanzados

```python
# Concatenar strings
palabras = ["Hola", "mundo", "de", "Python"]
frase = reduce(lambda x, y: x + " " + y, palabras)
print(frase)  # "Hola mundo de Python"

# Contar ocurrencias
letras = "programacion"
contador = reduce(
    lambda acc, letra: {**acc, letra: acc.get(letra, 0) + 1},
    letras,
    {}
)
print(contador)  # {'p': 1, 'r': 3, 'o': 2, 'g': 1, 'a': 3, 'm': 1, 'c': 1, 'i': 2, 'n': 1}

# Aplanar lista de listas
listas = [[1, 2], [3, 4], [5, 6]]
aplanada = reduce(lambda x, y: x + y, listas)
print(aplanada)  # [1, 2, 3, 4, 5, 6]
```

## 4. Sorted - Ordenar Elementos

La función `sorted()` retorna una nueva lista ordenada a partir de un iterable.

### Sintaxis
```python
sorted(iterable, key=None, reverse=False)
```

### Ejemplos Básicos

```python
# Ordenar números
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
ordenados = sorted(numeros)
print(ordenados)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Orden descendente
descendente = sorted(numeros, reverse=True)
print(descendente)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Ordenar strings
palabras = ["python", "java", "go", "rust"]
ordenadas = sorted(palabras)
print(ordenadas)  # ['go', 'java', 'python', 'rust']
```

### Uso del Parámetro key

```python
# Ordenar por longitud
palabras = ["python", "java", "javascript", "go", "rust"]
por_longitud = sorted(palabras, key=len)
print(por_longitud)  # ['go', 'java', 'rust', 'python', 'javascript']

# Ordenar por último carácter
por_ultimo = sorted(palabras, key=lambda x: x[-1])
print(por_ultimo)  # ['java', 'go', 'rust', 'python', 'javascript']

# Ordenar números por su valor absoluto
numeros = [-5, 2, -1, 3, -4]
por_absoluto = sorted(numeros, key=abs)
print(por_absoluto)  # [-1, 2, 3, -4, -5]
```

### Ejemplos Avanzados

```python
# Ordenar diccionarios
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 19, "nota": 7.2},
    {"nombre": "María", "edad": 21, "nota": 9.1},
    {"nombre": "Carlos", "edad": 18, "nota": 6.8}
]

# Por nota (descendente)
por_nota = sorted(estudiantes, key=lambda x: x["nota"], reverse=True)

# Por edad y luego por nota
por_edad_nota = sorted(estudiantes, key=lambda x: (x["edad"], x["nota"]))

# Ordenamiento personalizado complejo
def criterio_complejo(estudiante):
    # Primero por nota (descendente), luego por edad (ascendente)
    return (-estudiante["nota"], estudiante["edad"])

complejo = sorted(estudiantes, key=criterio_complejo)
```

## 5. Find - Encontrar Elementos

Python no tiene una función `find()` built-in, pero podemos implementarla usando otras técnicas.

### Implementaciones de Find

```python
# Usando next() con filter()
def find(predicate, iterable):
    """Encuentra el primer elemento que cumple la condición"""
    return next(filter(predicate, iterable), None)

# Usando next() con generador
def find_gen(predicate, iterable):
    """Encuentra usando generador"""
    return next((x for x in iterable if predicate(x)), None)

# Usando un bucle tradicional
def find_loop(predicate, iterable):
    """Encuentra usando bucle"""
    for item in iterable:
        if predicate(item):
            return item
    return None
```

### Ejemplos de Uso

```python
numeros = [1, 3, 5, 8, 9, 12, 15]

# Encontrar primer número par
primer_par = find(lambda x: x % 2 == 0, numeros)
print(primer_par)  # 8

# Encontrar primer número mayor a 10
mayor_diez = find(lambda x: x > 10, numeros)
print(mayor_diez)  # 12

# Con diccionarios
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 19, "nota": 7.2},
    {"nombre": "María", "edad": 21, "nota": 9.1}
]

# Encontrar estudiante por nombre
ana = find(lambda est: est["nombre"] == "Ana", estudiantes)
print(ana)  # {"nombre": "Ana", "edad": 20, "nota": 8.5}

# Encontrar primer estudiante con nota > 9
excelente = find(lambda est: est["nota"] > 9.0, estudiantes)
```

## Combinando Funciones

La verdadera potencia viene al combinar estas funciones:

### Ejemplo: Procesamiento de Datos

```python
from functools import reduce

# Dataset de ventas
ventas = [
    {"producto": "Laptop", "categoria": "Tecnologia", "precio": 1000, "cantidad": 2},
    {"producto": "Mouse", "categoria": "Tecnologia", "precio": 25, "cantidad": 10},
    {"producto": "Libro", "categoria": "Educacion", "precio": 15, "cantidad": 5},
    {"producto": "Tablet", "categoria": "Tecnologia", "precio": 300, "cantidad": 3},
    {"producto": "Curso", "categoria": "Educacion", "precio": 50, "cantidad": 8}
]

# Pipeline de procesamiento funcional
resultado = reduce(
    lambda acc, venta: acc + venta["total"],
    map(
        lambda v: {**v, "total": v["precio"] * v["cantidad"]},
        filter(lambda v: v["categoria"] == "Tecnologia", ventas)
    ),
    0
)

print(f"Total de ventas en Tecnología: ${resultado}")  # $3900
```

### Ejemplo: Análisis de Texto

```python
texto = "Python es un lenguaje de programación potente y versátil"

# Pipeline funcional para análisis
palabras = texto.lower().split()

# Análisis completo
analisis = {
    "total_palabras": len(palabras),
    "palabras_largas": len(list(filter(lambda p: len(p) > 5, palabras))),
    "longitud_promedio": sum(map(len, palabras)) / len(palabras),
    "palabra_mas_larga": max(palabras, key=len),
    "palabras_ordenadas": sorted(set(palabras), key=len, reverse=True)
}

print(analisis)
```

## Ejercicios Prácticos

### Ejercicio 1: Procesamiento de Números
```python
# Dado el siguiente lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 1. Filtrar solo números impares
# 2. Elevar cada número al cubo
# 3. Encontrar la suma total
# 4. Encontrar el número más grande después de las transformaciones

# Solución:
impares = filter(lambda x: x % 2 != 0, numeros)
cubos = map(lambda x: x ** 3, impares)
lista_cubos = list(cubos)
suma_total = reduce(lambda x, y: x + y, lista_cubos)
maximo = max(lista_cubos)
```

### Ejercicio 2: Gestión de Inventario
```python
inventario = [
    {"producto": "Laptop", "precio": 800, "stock": 5, "categoria": "Electrónicos"},
    {"producto": "Ratón", "precio": 20, "stock": 50, "categoria": "Electrónicos"},
    {"producto": "Libro Python", "precio": 35, "stock": 15, "categoria": "Libros"},
    {"producto": "Monitor", "precio": 200, "stock": 8, "categoria": "Electrónicos"},
    {"producto": "Teclado", "precio": 60, "stock": 25, "categoria": "Electrónicos"}
]

# Tareas:
# 1. Filtrar productos de categoría "Electrónicos"
# 2. Ordenar por precio descendente
# 3. Calcular valor total del inventario electrónico
# 4. Encontrar el producto más caro

# Tu solución aquí...
```

### Ejercicio 3: Análisis de Estudiantes
```python
estudiantes = [
    {"nombre": "Ana García", "notas": [8.5, 9.0, 7.5, 8.8], "edad": 20},
    {"nombre": "Luis Rodríguez", "notas": [7.2, 6.8, 8.1, 7.5], "edad": 19},
    {"nombre": "María López", "notas": [9.1, 9.5, 8.9, 9.2], "edad": 21},
    {"nombre": "Carlos Martín", "notas": [6.5, 7.0, 6.8, 7.2], "edad": 18}
]

# Tareas:
# 1. Calcular promedio de cada estudiante
# 2. Filtrar estudiantes con promedio >= 8.0
# 3. Ordenar por promedio descendente
# 4. Encontrar el estudiante más joven entre los de alto rendimiento

# Tu solución aquí...
```

## Consejos y Mejores Prácticas

### 1. Cuándo Usar Cada Función
- **filter()**: Para seleccionar elementos que cumplen una condición
- **map()**: Para transformar todos los elementos de una colección
- **reduce()**: Para combinar elementos en un solo valor
- **sorted()**: Para ordenar elementos según un criterio
- **find()**: Para encontrar el primer elemento que cumple una condición

### 2. Legibilidad vs. Rendimiento
```python
# Más legible pero menos eficiente
resultado = list(map(lambda x: x * 2, filter(lambda x: x > 5, numeros)))

# Más eficiente usando generadores
resultado = [x * 2 for x in numeros if x > 5]
```

### 3. Evitar Efectos Secundarios
```python
# Malo: modifica estado externo
contador = 0
def incrementar(x):
    global contador
    contador += 1
    return x * 2

# Bueno: función pura
def duplicar(x):
    return x * 2
```

### 4. Usar Type Hints
```python
from typing import List, Callable, Optional, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def mi_map(func: Callable[[T], U], items: List[T]) -> List[U]:
    return list(map(func, items))

def mi_filter(predicate: Callable[[T], bool], items: List[T]) -> List[T]:
    return list(filter(predicate, items))
```

## Conclusión

La programación funcional en Python nos proporciona herramientas poderosas para escribir código más expresivo y mantenible. Las funciones `filter()`, `map()`, `reduce()`, `sorted()` y las técnicas para implementar `find()` son fundamentales para dominar este paradigma.

### Puntos Clave:
- Las funciones de orden superior permiten código más abstracto y reutilizable
- La composición de funciones crea pipelines de procesamiento elegantes
- Las funciones puras son más fáciles de testear y debuggear
- La programación funcional complementa otros paradigmas en Python

### Recursos Adicionales:
- Documentación oficial de Python sobre funciones built-in
- Módulo `functools` para más herramientas funcionales
- Módulo `itertools` para iteradores especializados
- Librerías como `toolz` para programación funcional avanzada

¡Practica estos conceptos y verás cómo tu código Python se vuelve más elegante y expresivo!