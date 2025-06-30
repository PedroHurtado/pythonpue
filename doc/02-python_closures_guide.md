# Guía Completa de Clausuras en Python

## Tabla de Contenidos

1. [¿Qué es una Clausura?](#qué-es-una-clausura)
2. [Conceptos Previos](#conceptos-previos)
3. [Clausuras Básicas](#clausuras-básicas)
4. [Ejemplos Prácticos](#ejemplos-prácticos)
5. [Clausuras con Múltiples Variables](#clausuras-con-múltiples-variables)
6. [Clausuras vs Clases](#clausuras-vs-clases)
7. [Casos de Uso Avanzados](#casos-de-uso-avanzados)
8. [Ventajas y Desventajas](#ventajas-y-desventajas)
9. [Inspección de Clausuras](#inspección-de-clausuras)
10. [Ejercicios Prácticos](#ejercicios-prácticos)

## ¿Qué es una Clausura?

Una **clausura** (closure) es una función que "captura" y "recuerda" variables de su ámbito externo, incluso después de que ese ámbito haya terminado de ejecutarse. Es como si la función llevara consigo una "mochila" con las variables que necesita.

### Características Principales:
- La función interna accede a variables de la función externa
- Las variables del ámbito externo permanecen "vivas" después de que la función externa termine
- Cada clausura mantiene su propia copia de las variables capturadas
- Permite crear funciones con "memoria" o estado persistente

## Conceptos Previos

### Ámbito de Variables (Scope)

En Python, las variables tienen diferentes ámbitos:

```python
# Variable global
x = 10

def funcion_externa():
    # Variable local de función externa
    y = 20
    
    def funcion_interna():
        # Variable local de función interna
        z = 30
        # Puede acceder a x (global), y (nonlocal), z (local)
        print(f"x: {x}, y: {y}, z: {z}")
    
    funcion_interna()

funcion_externa()  # Salida: x: 10, y: 20, z: 30
```

### Funciones Anidadas

Las funciones anidadas son el fundamento de las clausuras:

```python
def exterior():
    mensaje = "Hola desde función exterior"
    
    def interior():
        print(mensaje)  # Accede a variable de función exterior
    
    return interior  # Retorna la función, no la ejecuta

mi_funcion = exterior()
mi_funcion()  # Salida: "Hola desde función exterior"
```

### La Palabra Clave `nonlocal`

Para modificar variables del ámbito externo, usamos `nonlocal`:

```python
def exterior():
    contador = 0
    
    def incrementar():
        nonlocal contador  # Permite modificar la variable externa
        contador += 1
        return contador
    
    return incrementar

inc = exterior()
print(inc())  # 1
print(inc())  # 2
print(inc())  # 3
```

## Clausuras Básicas

### Ejemplo Simple: Factory de Multiplicadores

```python
def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor  # 'factor' es capturado por la clausura
    return multiplicar

# Crear clausuras específicas
doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
cuadruple = crear_multiplicador(4)

print(doble(5))      # 10 (5 * 2)
print(triple(5))     # 15 (5 * 3)
print(cuadruple(5))  # 20 (5 * 4)

# La variable 'factor' sigue "viva" en cada clausura
print(doble(10))     # 20
print(triple(10))    # 30
```

### Ejemplo con Estado: Contador

```python
def crear_contador(inicial=0, paso=1):
    def incrementar():
        nonlocal inicial
        inicial += paso
        return inicial
    
    def decrementar():
        nonlocal inicial
        inicial -= paso
        return inicial
    
    def obtener_valor():
        return inicial
    
    def resetear():
        nonlocal inicial
        inicial = 0
    
    # Retornar diccionario con métodos
    return {
        'incrementar': incrementar,
        'decrementar': decrementar,
        'valor': obtener_valor,
        'resetear': resetear
    }

contador1 = crear_contador()
contador2 = crear_contador(100, 5)

print(contador1['incrementar']())  # 1
print(contador1['incrementar']())  # 2
print(contador2['incrementar']())  # 105
print(contador1['valor']())        # 2
print(contador2['valor']())        # 105
```

## Ejemplos Prácticos

### 1. Factory de Validadores

```python
def crear_validador(min_length=0, max_length=float('inf'), patron=None):
    import re
    
    def validar(texto):
        errores = []
        
        if len(texto) < min_length:
            errores.append(f"Muy corto. Mínimo {min_length} caracteres")
        
        if len(texto) > max_length:
            errores.append(f"Muy largo. Máximo {max_length} caracteres")
        
        if patron and not re.match(patron, texto):
            errores.append("No cumple con el patrón requerido")
        
        return {
            'valido': len(errores) == 0,
            'errores': errores,
            'texto': texto
        }
    
    return validar

# Crear validadores específicos
validar_password = crear_validador(8, 20, r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')
validar_email = crear_validador(5, 254, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
validar_username = crear_validador(3, 15, r'^[a-zA-Z0-9_]+$')

# Usar validadores
print(validar_password("123"))                    # Muy corto, no cumple patrón
print(validar_password("MiPassword123"))          # Válido
print(validar_email("usuario@ejemplo.com"))      # Válido
print(validar_username("usuario_123"))           # Válido
```

### 2. Sistema de Configuración de Formateo

```python
def crear_formateador(prefijo="", sufijo="", transformar=None):
    def formatear(texto):
        # Aplicar transformación si existe
        if transformar:
            texto = transformar(texto)
        
        return f"{prefijo}{texto}{sufijo}"
    
    return formatear

# Diferentes formateadores
html_bold = crear_formateador("<b>", "</b>")
html_italic = crear_formateador("<i>", "</i>")
markdown_code = crear_formateador("`", "`")
mayusculas_parentesis = crear_formateador("(", ")", str.upper)
titulo = crear_formateador("=== ", " ===", str.title)

print(html_bold("importante"))           # "<b>importante</b>"
print(html_italic("énfasis"))            # "<i>énfasis</i>"
print(markdown_code("codigo"))           # "`codigo`"
print(mayusculas_parentesis("nota"))     # "(NOTA)"
print(titulo("mi título"))               # "=== Mi Título ==="
```

### 3. Acumulador de Estadísticas

```python
def crear_estadisticas():
    numeros = []
    
    def agregar(numero):
        numeros.append(numero)
        n = len(numeros)
        suma = sum(numeros)
        promedio = suma / n
        
        return {
            "ultimo": numero,
            "cantidad": n,
            "suma": suma,
            "promedio": round(promedio, 2),
            "minimo": min(numeros),
            "maximo": max(numeros),
            "rango": max(numeros) - min(numeros)
        }
    
    def obtener_todos():
        return numeros.copy()
    
    def limpiar():
        nonlocal numeros
        numeros = []
        return "Estadísticas limpiadas"
    
    def obtener_resumen():
        if not numeros:
            return "No hay datos"
        
        n = len(numeros)
        suma = sum(numeros)
        return {
            "total_numeros": n,
            "suma_total": suma,
            "promedio": round(suma / n, 2),
            "valor_minimo": min(numeros),
            "valor_maximo": max(numeros)
        }
    
    # Agregar métodos adicionales como atributos
    agregar.obtener_todos = obtener_todos
    agregar.limpiar = limpiar
    agregar.resumen = obtener_resumen
    
    return agregar

# Uso del acumulador
stats = crear_estadisticas()

print(stats(10))    # Primera entrada
print(stats(20))    # Segunda entrada
print(stats(5))     # Tercera entrada
print(stats(15))    # Cuarta entrada

print("\nTodos los números:", stats.obtener_todos())
print("Resumen:", stats.resumen())
```

## Clausuras con Múltiples Variables

### Sistema de Descuentos y Precios

```python
def crear_calculadora_precio(precio_base, descuento_porcentaje=0, impuesto_porcentaje=0):
    def calcular(cantidad=1, descuento_adicional=0, mostrar_detalles=False):
        # Todas estas variables son capturadas por la clausura
        subtotal = precio_base * cantidad
        descuento_total = descuento_porcentaje + descuento_adicional
        precio_con_descuento = subtotal * (1 - descuento_total / 100)
        impuesto_aplicado = precio_con_descuento * (impuesto_porcentaje / 100)
        precio_final = precio_con_descuento + impuesto_aplicado
        
        resultado = {
            "precio_final": round(precio_final, 2)
        }
        
        if mostrar_detalles:
            resultado.update({
                "precio_base": precio_base,
                "cantidad": cantidad,
                "subtotal": subtotal,
                "descuento_porcentaje": descuento_total,
                "precio_con_descuento": round(precio_con_descuento, 2),
                "impuesto_porcentaje": impuesto_porcentaje,
                "impuesto_aplicado": round(impuesto_aplicado, 2)
            })
        
        return resultado
    
    return calcular

# Productos con diferentes configuraciones
laptop = crear_calculadora_precio(1000, 10, 21)    # €1000, 10% desc, 21% IVA
mouse = crear_calculadora_precio(25, 5, 21)        # €25, 5% desc, 21% IVA
libro = crear_calculadora_precio(35, 0, 4)         # €35, sin desc, 4% IVA

print("Laptop (2 unidades):", laptop(2, mostrar_detalles=True))
print("Laptop (1 unidad, 5% desc adicional):", laptop(1, 5))
print("Mouse (3 unidades):", mouse(3))
print("Libro:", libro(mostrar_detalles=True))
```

### Factory de Conexiones de Base de Datos

```python
def crear_conexion_db(host, puerto, usuario, base_datos):
    conexiones_activas = []
    configuracion = {
        'host': host,
        'puerto': puerto,
        'usuario': usuario,
        'base_datos': base_datos,
        'timeout': 30
    }
    
    def conectar(password, timeout=None):
        if timeout:
            configuracion['timeout'] = timeout
        
        # Simular conexión
        conexion_id = len(conexiones_activas) + 1
        conexion = {
            'id': conexion_id,
            'config': configuracion.copy(),
            'estado': 'conectado',
            'password': '***oculta***'  # No almacenar password real
        }
        conexiones_activas.append(conexion)
        
        return {
            'conexion_id': conexion_id,
            'estado': 'conectado',
            'host': host,
            'base_datos': base_datos
        }
    
    def desconectar(conexion_id):
        for conn in conexiones_activas:
            if conn['id'] == conexion_id:
                conn['estado'] = 'desconectado'
                return f"Conexión {conexion_id} desconectada"
        return f"Conexión {conexion_id} no encontrada"
    
    def obtener_estado():
        activas = [c for c in conexiones_activas if c['estado'] == 'conectado']
        return {
            'configuracion': configuracion,
            'conexiones_totales': len(conexiones_activas),
            'conexiones_activas': len(activas),
            'detalles_activas': [{'id': c['id'], 'estado': c['estado']} for c in activas]
        }
    
    # Retornar interfaz
    return {
        'conectar': conectar,
        'desconectar': desconectar,
        'estado': obtener_estado
    }

# Uso del factory
db_prod = crear_conexion_db('prod.ejemplo.com', 5432, 'admin', 'produccion')
db_test = crear_conexion_db('test.ejemplo.com', 5432, 'test_user', 'testing')

# Conectar
conn1 = db_prod['conectar']('password123')
conn2 = db_prod['conectar']('password123')
conn3 = db_test['conectar']('testpass')

print("Estado DB Producción:", db_prod['estado']())
print("Estado DB Testing:", db_test['estado']())
```

## Clausuras vs Clases

### Implementación con Clase

```python
class ContadorClase:
    def __init__(self, inicial=0, paso=1):
        self.valor = inicial
        self.paso = paso
        self.historial = []
    
    def incrementar(self):
        self.valor += self.paso
        self.historial.append(('incrementar', self.valor))
        return self.valor
    
    def decrementar(self):
        self.valor -= self.paso
        self.historial.append(('decrementar', self.valor))
        return self.valor
    
    def obtener_valor(self):
        return self.valor
    
    def obtener_historial(self):
        return self.historial.copy()
    
    def resetear(self):
        anterior = self.valor
        self.valor = 0
        self.historial.append(('resetear', self.valor))
        return f"Reseteado de {anterior} a {self.valor}"
```

### Implementación con Clausura

```python
def crear_contador_clausura(inicial=0, paso=1):
    valor = inicial
    historial = []
    
    def incrementar():
        nonlocal valor
        valor += paso
        historial.append(('incrementar', valor))
        return valor
    
    def decrementar():
        nonlocal valor
        valor -= paso
        historial.append(('decrementar', valor))
        return valor
    
    def obtener_valor():
        return valor
    
    def obtener_historial():
        return historial.copy()
    
    def resetear():
        nonlocal valor
        anterior = valor
        valor = 0
        historial.append(('resetear', valor))
        return f"Reseteado de {anterior} a {valor}"
    
    return {
        'incrementar': incrementar,
        'decrementar': decrementar,
        'valor': obtener_valor,
        'historial': obtener_historial,
        'resetear': resetear
    }

# Comparación de uso
contador_clase = ContadorClase(10, 2)
contador_clausura = crear_contador_clausura(10, 2)

# Ambos funcionan de manera similar
print("Clase:", contador_clase.incrementar())           # 12
print("Clausura:", contador_clausura['incrementar']())  # 12
```

### ¿Cuándo usar cada uno?

**Usar Clausuras cuando:**
- Necesitas funcionalidad simple con estado
- Quieres encapsular datos privados
- Prefieres un enfoque funcional
- El estado es limitado y específico

**Usar Clases cuando:**
- Tienes estado complejo con múltiples propiedades
- Necesitas herencia o polimorfismo
- Quieres métodos especiales (__str__, __len__, etc.)
- El código será mantenido por equipos grandes

## Casos de Uso Avanzados

### 1. Memoización (Cache) Inteligente

```python
def crear_cache_inteligente(max_size=100, ttl_seconds=3600):
    import time
    
    cache = {}
    accesos = {}
    
    def memoizar(func):
        def wrapper(*args, **kwargs):
            # Crear clave única para argumentos
            key = str(args) + str(sorted(kwargs.items()))
            ahora = time.time()
            
            # Limpiar entradas expiradas
            keys_expiradas = [
                k for k, (timestamp, _) in cache.items() 
                if ahora - timestamp > ttl_seconds
            ]
            for k in keys_expiradas:
                del cache[k]
                if k in accesos:
                    del accesos[k]
            
            # Verificar si está en cache y no ha expirado
            if key in cache:
                timestamp, resultado = cache[key]
                if ahora - timestamp <= ttl_seconds:
                    accesos[key] = accesos.get(key, 0) + 1
                    print(f"Cache HIT para {func.__name__}{args}")
                    return resultado
            
            # Limpiar cache si está lleno
            if len(cache) >= max_size:
                # Eliminar el elemento menos accedido
                key_menos_usado = min(accesos.items(), key=lambda x: x[1])[0]
                del cache[key_menos_usado]
                del accesos[key_menos_usado]
            
            # Calcular y cachear resultado
            print(f"Cache MISS para {func.__name__}{args}")
            resultado = func(*args, **kwargs)
            cache[key] = (ahora, resultado)
            accesos[key] = 1
            
            return resultado
        
        # Métodos para inspeccionar el cache
        wrapper.stats = lambda: {
            'tamaño_cache': len(cache),
            'max_size': max_size,
            'ttl_seconds': ttl_seconds,
            'accesos_totales': sum(accesos.values()),
            'entradas_populares': sorted(accesos.items(), key=lambda x: x[1], reverse=True)[:5]
        }
        
        wrapper.limpiar = lambda: cache.clear() or accesos.clear()
        
        return wrapper
    
    return memoizar

# Uso del cache inteligente
cache_fibonacci = crear_cache_inteligente(max_size=50, ttl_seconds=300)

@cache_fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@cache_fibonacci
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Probar el cache
print(fibonacci(10))
print(fibonacci(8))   # Algunos valores ya están en cache
print(factorial(5))
print(fibonacci.stats())
```

### 2. Sistema de Middleware Configurable

```python
def crear_pipeline_middleware():
    middlewares = []
    
    def agregar_middleware(nombre, before=None, after=None, error_handler=None):
        def decorador(func):
            middleware = {
                'nombre': nombre,
                'func': func,
                'before': before,
                'after': after,
                'error_handler': error_handler
            }
            middlewares.append(middleware)
            return func
        return decorador
    
    def ejecutar_pipeline(funcion_principal):
        def wrapper(*args, **kwargs):
            contexto = {'args': args, 'kwargs': kwargs, 'resultado': None, 'errores': []}
            
            # Ejecutar hooks 'before'
            for middleware in middlewares:
                if middleware['before']:
                    try:
                        middleware['before'](contexto)
                    except Exception as e:
                        contexto['errores'].append(f"Error en before de {middleware['nombre']}: {e}")
            
            # Ejecutar función principal
            try:
                contexto['resultado'] = funcion_principal(*contexto['args'], **contexto['kwargs'])
            except Exception as e:
                contexto['errores'].append(f"Error en función principal: {e}")
                
                # Ejecutar error handlers
                for middleware in middlewares:
                    if middleware['error_handler']:
                        try:
                            middleware['error_handler'](e, contexto)
                        except Exception as handler_error:
                            contexto['errores'].append(f"Error en handler de {middleware['nombre']}: {handler_error}")
            
            # Ejecutar hooks 'after'
            for middleware in middlewares:
                if middleware['after']:
                    try:
                        middleware['after'](contexto)
                    except Exception as e:
                        contexto['errores'].append(f"Error en after de {middleware['nombre']}: {e}")
            
            return contexto['resultado']
        
        return wrapper
    
    def obtener_middlewares():
        return [m['nombre'] for m in middlewares]
    
    return {
        'agregar': agregar_middleware,
        'ejecutar': ejecutar_pipeline,
        'listar': obtener_middlewares
    }

# Crear pipeline
pipeline = crear_pipeline_middleware()

# Definir middlewares
@pipeline['agregar']('logging', 
                    before=lambda ctx: print(f"Iniciando con args: {ctx['args']}"),
                    after=lambda ctx: print(f"Terminado con resultado: {ctx['resultado']}"))
def log_middleware():
    pass

@pipeline['agregar']('auth',
                    before=lambda ctx: print("Verificando autenticación..."),
                    error_handler=lambda e, ctx: print(f"Error de auth: {e}"))
def auth_middleware():
    pass

@pipeline['agregar']('cache',
                    after=lambda ctx: print("Guardando en cache..."))
def cache_middleware():
    pass

# Función principal
@pipeline['ejecutar']
def procesar_datos(datos, formato='json'):
    print(f"Procesando {datos} en formato {formato}")
    return f"Procesado: {datos}"

# Ejecutar
resultado = procesar_datos("información importante", formato="xml")
print(f"Middlewares activos: {pipeline['listar']()}")
```

### 3. Factory de Rate Limiters

```python
def crear_rate_limiter(max_calls=10, tiempo_ventana=60, estrategia='sliding_window'):
    import time
    from collections import deque
    
    if estrategia == 'sliding_window':
        llamadas = deque()
        
        def verificar():
            ahora = time.time()
            # Remover llamadas fuera de la ventana
            while llamadas and ahora - llamadas[0] > tiempo_ventana:
                llamadas.popleft()
            
            if len(llamadas) < max_calls:
                llamadas.append(ahora)
                return True
            return False
    
    elif estrategia == 'token_bucket':
        tokens = max_calls
        ultima_actualizacion = time.time()
        
        def verificar():
            nonlocal tokens, ultima_actualizacion
            ahora = time.time()
            
            # Agregar tokens basado en tiempo transcurrido
            tiempo_transcurrido = ahora - ultima_actualizacion
            tokens_a_agregar = tiempo_transcurrido * (max_calls / tiempo_ventana)
            tokens = min(max_calls, tokens + tokens_a_agregar)
            ultima_actualizacion = ahora
            
            if tokens >= 1:
                tokens -= 1
                return True
            return False
    
    else:  # fixed_window
        ventana_actual = 0
        contador = 0
        
        def verificar():
            nonlocal ventana_actual, contador
            ahora = time.time()
            ventana = int(ahora // tiempo_ventana)
            
            if ventana != ventana_actual:
                ventana_actual = ventana
                contador = 0
            
            if contador < max_calls:
                contador += 1
                return True
            return False
    
    def obtener_estado():
        if estrategia == 'sliding_window':
            return {
                'estrategia': estrategia,
                'llamadas_en_ventana': len(llamadas),
                'max_calls': max_calls,
                'tiempo_ventana': tiempo_ventana
            }
        elif estrategia == 'token_bucket':
            return {
                'estrategia': estrategia,
                'tokens_disponibles': int(tokens),
                'max_tokens': max_calls,
                'tiempo_ventana': tiempo_ventana
            }
        else:
            return {
                'estrategia': estrategia,
                'llamadas_en_ventana': contador,
                'max_calls': max_calls,
                'tiempo_ventana': tiempo_ventana
            }
    
    verificar.estado = obtener_estado
    return verificar

# Diferentes estrategias de rate limiting
limiter_sliding = crear_rate_limiter(5, 60, 'sliding_window')    # 5 calls/min sliding
limiter_token = crear_rate_limiter(10, 60, 'token_bucket')       # 10 tokens/min
limiter_fixed = crear_rate_limiter(3, 30, 'fixed_window')        # 3 calls/30s fixed

def hacer_request(limiter, nombre):
    if limiter():
        print(f"✅ {nombre}: Request permitido - {limiter.estado()}")
        return True
    else:
        print(f"❌ {nombre}: Rate limit excedido - {limiter.estado()}")
        return False

# Simular requests
import time
for i in range(8):
    print(f"\n--- Request {i+1} ---")
    hacer_request(limiter_sliding, "Sliding Window")
    hacer_request(limiter_token, "Token Bucket")
    hacer_request(limiter_fixed, "Fixed Window")
    time.sleep(1)
```

## Ventajas y Desventajas

### Ventajas

#### 1. Encapsulación Natural
```python
def crear_cuenta_bancaria(saldo_inicial):
    saldo = saldo_inicial  # Variable privada, no accesible desde afuera
    
    def depositar(cantidad):
        nonlocal saldo
        if cantidad > 0:
            saldo += cantidad
            return f"Depositado: ${cantidad}. Saldo actual: ${saldo}"
        return "Cantidad debe ser positiva"
    
    def retirar(cantidad):
        nonlocal saldo
        if 0 < cantidad <= saldo:
            saldo -= cantidad
            return f"Retirado: ${cantidad}. Saldo actual: ${saldo}"
        return "Fondos insuficientes o cantidad inválida"
    
    def consultar_saldo():
        return saldo
    
    return {
        'depositar': depositar,
        'retirar': retirar,
        'saldo': consultar_saldo
    }

cuenta = crear_cuenta_bancaria(1000)
# No hay manera de acceder directamente a 'saldo'
print(cuenta['saldo']())  # 1000
```

#### 2. Estado Persistente
Las clausuras mantienen estado entre llamadas sin necesidad de variables globales.

#### 3. Configuración Flexible
Permiten crear funciones especializadas fácilmente.

#### 4. Composición Elegante
Se pueden combinar fácilmente para crear comportamientos complejos.

### Desventajas

#### 1. Uso de Memoria
```python
def crear_clausura_pesada():
    datos_grandes = list(range(1000000))  # Lista muy grande
    
    def procesar(x):
        return x * 2  # No usa 'datos_grandes' pero los mantiene en memoria
    
    return procesar

# Esta clausura mantiene en memoria la lista grande innecesariamente
procesador = crear_clausura_pesada()
```

#### 2. Dificultad para Debugging
```python
def clausura_compleja(a, b, c):
    def nivel1(x):
        def nivel2(y):
            def nivel3(z):
                return a + b + c + x + y + z  # Variables de múltiples niveles
            return nivel3
        return nivel2
    return nivel1

# Difícil de debuggear y entender el flujo
resultado = clausura_compleja(1, 2, 3)(4)(5)(6)
```

#### 3. Complejidad Conceptual
Pueden ser difíciles de entender para programadores novatos.

## Inspección de Clausuras

Python proporciona herramientas para inspeccionar clausuras:

### Métodos de Inspección

```python
def crear_clausura_ejemplo(x, y, z):
    def clausura(a, b):
        return x + y + z + a + b
    return clausura

mi_clausura = crear_clausura_ejemplo(10, 20, 30)

# 1. Variables capturadas
print("Closure cells:", mi_clausura.__closure__)
if mi_clausura.__closure__:
    valores = [cell.cell_contents for cell in mi_clausura.__closure__]
    print("Valores capturados:", valores)  # [10, 20, 30]

# 2. Nombres de variables libres
print("Variables libres:", mi_clausura.__code__.co_freevars)  # ('x', 'y', 'z')

# 3. Información del código
print("Nombres de variables:", mi_clausura.__code__.co_varnames)
print("Número de argumentos:", mi_clausura.__code__.co_argcount)
```

### Herramienta de Debug para Clausuras

```python
def debug_clausura(clausura):
    """Función para debuggear clausuras"""
    info = {
        'nombre': clausura.__name__,
        'doc': clausura.__doc__