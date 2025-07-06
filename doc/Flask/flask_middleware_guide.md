# Cómo crear Middleware en Flask

En Flask, un middleware es una función que se ejecuta antes o después de cada request. Aquí te muestro las principales formas de crear middleware:

## 1. Usando decoradores `@app.before_request` y `@app.after_request`

```python
from flask import Flask, request, g
import time

app = Flask(__name__)

@app.before_request
def before_request():
    # Se ejecuta antes de cada request
    g.start_time = time.time()
    print(f"Request iniciado: {request.method} {request.path}")

@app.after_request
def after_request(response):
    # Se ejecuta después de cada request
    duration = time.time() - g.start_time
    print(f"Request completado en {duration:.2f} segundos")
    return response

@app.route('/')
def home():
    return "¡Hola mundo!"
```

## 2. Middleware personalizado como clase

```python
from flask import Flask, request, jsonify

class AuthMiddleware:
    def __init__(self, app):
        self.app = app
        self.app.before_request(self.authenticate)
    
    def authenticate(self):
        # Rutas que no requieren autenticación
        exempt_routes = ['/login', '/register']
        
        if request.endpoint in exempt_routes:
            return
        
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token requerido'}), 401
        
        # Aquí validarías el token
        if token != 'Bearer mi_token_secreto':
            return jsonify({'error': 'Token inválido'}), 401

app = Flask(__name__)
AuthMiddleware(app)

@app.route('/login')
def login():
    return "Página de login"

@app.route('/dashboard')
def dashboard():
    return "Dashboard - requiere autenticación"
```

## 3. Middleware para logging completo

```python
from flask import Flask, request, g
import logging
import time

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.before_request
def log_request_info():
    g.start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")
    logger.info(f"Headers: {dict(request.headers)}")

@app.after_request
def log_response_info(response):
    duration = time.time() - g.start_time
    logger.info(f"Response: {response.status_code} - {duration:.2f}s")
    return response

@app.route('/')
def home():
    return "¡Hola mundo!"
```

## 4. Middleware para CORS

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Método 1: Usando flask-cors
CORS(app)

# Método 2: Middleware manual para CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
```

## 5. Middleware usando WSGI

```python
from flask import Flask

class TimingMiddleware:
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        import time
        start_time = time.time()
        
        def new_start_response(status, response_headers):
            duration = time.time() - start_time
            response_headers.append(('X-Response-Time', str(duration)))
            return start_response(status, response_headers)
        
        return self.app(environ, new_start_response)

app = Flask(__name__)
app.wsgi_app = TimingMiddleware(app.wsgi_app)

@app.route('/')
def home():
    return "¡Hola mundo!"
```

## Orden de ejecución

1. `@app.before_first_request` (solo la primera vez)
2. `@app.before_request`
3. Vista/endpoint
4. `@app.after_request`
5. `@app.teardown_request`

## Consejos importantes

- El middleware `before_request` puede retornar una respuesta para interrumpir el flujo
- El middleware `after_request` debe siempre retornar el objeto response
- Usa `g` para compartir datos entre middleware y vistas
- Para aplicaciones grandes, considera usar Blueprints con middleware específico

## Casos de uso comunes

### Autenticación y autorización
```python
@app.before_request
def check_auth():
    if request.endpoint == 'login':
        return
    
    if 'user_id' not in session:
        return redirect('/login')
```

### Rate limiting
```python
from collections import defaultdict
import time

request_counts = defaultdict(list)

@app.before_request
def rate_limit():
    ip = request.remote_addr
    now = time.time()
    
    # Limpiar requests antiguos (más de 1 minuto)
    request_counts[ip] = [req_time for req_time in request_counts[ip] if now - req_time < 60]
    
    # Verificar límite (máximo 100 requests por minuto)
    if len(request_counts[ip]) >= 100:
        return jsonify({'error': 'Rate limit exceeded'}), 429
    
    request_counts[ip].append(now)
```

### Validación de contenido
```python
@app.before_request
def validate_json():
    if request.is_json and request.method in ['POST', 'PUT']:
        try:
            request.get_json()
        except:
            return jsonify({'error': 'Invalid JSON'}), 400
```

## Mejores prácticas

1. **Mantén el middleware ligero**: Evita operaciones costosas que ralenticen todas las requests
2. **Usa blueprints**: Para middleware específico de ciertas rutas
3. **Maneja errores**: Siempre incluye manejo de errores en tu middleware
4. **Documenta bien**: El middleware puede afectar toda la aplicación
5. **Testea exhaustivamente**: Asegúrate de que el middleware no rompa funcionalidad existente