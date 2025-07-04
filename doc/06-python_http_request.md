# HTTP Requests en Python: Guía Completa

## Introducción

En Python, el equivalente más directo de `fetch` de JavaScript es la librería **`requests`**. Esta guía te muestra cómo realizar llamadas HTTP usando las principales librerías disponibles.

## Librerías Disponibles

### 1. requests (Recomendado)
- **Instalación**: `pip install requests`
- La más popular y fácil de usar
- API intuitiva y completa
- Perfecta para la mayoría de casos de uso

### 2. urllib (Incluida)
- Viene preinstalada con Python
- Más verbosa pero sin dependencias externas
- Buena para casos simples

### 3. httpx (Moderna)
- **Instalación**: `pip install httpx`
- API similar a requests
- Soporte nativo para async/await
- Ideal para aplicaciones modernas

## Ejemplos con requests

### Configuración Básica

```python
import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
```

### GET - Obtener datos

```python
def get_example():
    try:
        response = requests.get(f"{BASE_URL}/posts/1")
        
        # Verificar que la petición fue exitosa
        response.raise_for_status()
        
        # Obtener datos como JSON
        data = response.json()
        print("GET Response:")
        print(json.dumps(data, indent=2))
        
        # Información adicional
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        
    except requests.RequestException as e:
        print(f"Error en GET: {e}")
```

### POST - Crear datos

```python
def post_example():
    try:
        # Datos a enviar
        data = {
            "title": "Mi nuevo post",
            "body": "Este es el contenido del post",
            "userId": 1
        }
        
        response = requests.post(
            f"{BASE_URL}/posts",
            headers=headers,
            json=data  # Automáticamente convierte a JSON
        )
        
        response.raise_for_status()
        
        result = response.json()
        print("POST Response:")
        print(json.dumps(result, indent=2))
        
    except requests.RequestException as e:
        print(f"Error en POST: {e}")
```

### PUT - Actualizar datos completos

```python
def put_example():
    try:
        # Datos actualizados
        data = {
            "id": 1,
            "title": "Post actualizado",
            "body": "Contenido completamente actualizado",
            "userId": 1
        }
        
        response = requests.put(
            f"{BASE_URL}/posts/1",
            headers=headers,
            json=data
        )
        
        response.raise_for_status()
        
        result = response.json()
        print("PUT Response:")
        print(json.dumps(result, indent=2))
        
    except requests.RequestException as e:
        print(f"Error en PUT: {e}")
```

### DELETE - Eliminar datos

```python
def delete_example():
    try:
        response = requests.delete(f"{BASE_URL}/posts/1")
        
        response.raise_for_status()
        
        print("DELETE Response:")
        print(f"Status Code: {response.status_code}")
        
        # DELETE puede devolver contenido vacío
        if response.text:
            print(f"Response body: {response.text}")
        else:
            print("Response body: (vacío)")
            
    except requests.RequestException as e:
        print(f"Error en DELETE: {e}")
```

### PATCH - Actualización parcial

```python
def patch_example():
    try:
        # Solo los campos que queremos actualizar
        data = {
            "title": "Título actualizado parcialmente"
        }
        
        response = requests.patch(
            f"{BASE_URL}/posts/1",
            headers=headers,
            json=data
        )
        
        response.raise_for_status()
        
        result = response.json()
        print("PATCH Response:")
        print(json.dumps(result, indent=2))
        
    except requests.RequestException as e:
        print(f"Error en PATCH: {e}")
```

## Ejemplo Avanzado con Autenticación

```python
def advanced_example():
    try:
        # Parámetros de consulta
        params = {
            "userId": 1,
            "limit": 5
        }
        
        # Headers con autenticación
        auth_headers = {
            **headers,
            "Authorization": "Bearer tu-token-aqui"
        }
        
        response = requests.get(
            f"{BASE_URL}/posts",
            headers=auth_headers,
            params=params,
            timeout=10  # Timeout en segundos
        )
        
        response.raise_for_status()
        
        data = response.json()
        print("Advanced GET Response:")
        print(f"Found {len(data)} posts")
        
    except requests.RequestException as e:
        print(f"Error en petición avanzada: {e}")
```

## Usando urllib (Librería Estándar)

```python
import urllib.request
import urllib.parse
import urllib.error

def urllib_example():
    try:
        # GET con urllib
        req = urllib.request.Request(
            f"{BASE_URL}/posts/1",
            headers={"Accept": "application/json"}
        )
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print("urllib GET Response:")
            print(json.dumps(data, indent=2))
            
    except urllib.error.URLError as e:
        print(f"Error con urllib: {e}")
```

## Usando httpx (Alternativa Moderna)

### Instalación
```bash
pip install httpx
```

### Ejemplo Síncrono
```python
import httpx

def httpx_example():
    try:
        # httpx tiene una API muy similar a requests
        response = httpx.get(f"{BASE_URL}/posts/1")
        response.raise_for_status()
        
        data = response.json()
        print("httpx GET Response:")
        print(json.dumps(data, indent=2))
        
    except httpx.RequestError as e:
        print(f"Error con httpx: {e}")
```

### Ejemplo Asíncrono
```python
import asyncio
import httpx

async def httpx_async_example():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts/1")
        response.raise_for_status()
        
        data = response.json()
        print("httpx Async GET Response:")
        print(json.dumps(data, indent=2))

# Para ejecutar:
# asyncio.run(httpx_async_example())
```

## Manejo de Errores

### Errores Comunes
```python
import requests

try:
    response = requests.get("https://api.ejemplo.com/datos")
    response.raise_for_status()  # Lanza excepción si status >= 400
    
except requests.exceptions.ConnectionError:
    print("Error de conexión")
except requests.exceptions.Timeout:
    print("Timeout de la petición")
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error general: {e}")
```

## Configuración de Sesiones

```python
# Para reutilizar configuración entre peticiones
session = requests.Session()
session.headers.update({
    "Authorization": "Bearer tu-token",
    "User-Agent": "Mi-App/1.0"
})

# Todas las peticiones usarán estos headers
response = session.get("https://api.ejemplo.com/datos")
```

## Comparación de Sintaxis

### requests vs urllib

**requests (simple):**
```python
response = requests.get("https://api.ejemplo.com/datos")
data = response.json()
```

**urllib (más verboso):**
```python
import urllib.request
import json

req = urllib.request.Request("https://api.ejemplo.com/datos")
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
```

## Mejores Prácticas

1. **Usa `requests` para la mayoría de casos**
2. **Siempre maneja excepciones**
3. **Usa timeouts** para evitar cuelgues
4. **Usa sesiones** para múltiples peticiones
5. **Verifica el status code** con `raise_for_status()`

## Instalación de Dependencias

```bash
# requests
pip install requests

# httpx (opcional)
pip install httpx

# urllib ya viene incluido con Python
```

## Ejemplo Completo Ejecutable

```python
import requests
import json

def main():
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # GET
    print("=== GET Example ===")
    response = requests.get(f"{BASE_URL}/posts/1")
    print(f"Status: {response.status_code}")
    print(f"Data: {response.json()}")
    
    # POST
    print("\n=== POST Example ===")
    data = {"title": "Nuevo post", "body": "Contenido", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    print(f"Status: {response.status_code}")
    print(f"Created: {response.json()}")
    
    # PUT
    print("\n=== PUT Example ===")
    data = {"id": 1, "title": "Post actualizado", "body": "Nuevo contenido", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=data)
    print(f"Status: {response.status_code}")
    print(f"Updated: {response.json()}")
    
    # DELETE
    print("\n=== DELETE Example ===")
    response = requests.delete(f"{BASE_URL}/posts/1")
    print(f"Status: {response.status_code}")
    print("Deleted successfully" if response.status_code == 200 else "Delete failed")

if __name__ == "__main__":
    main()
```

---

**Nota**: Esta guía cubre las principales formas de realizar HTTP requests en Python. Para casos de uso específicos, consulta la documentación oficial de cada librería.