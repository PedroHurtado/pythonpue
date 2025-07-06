# 🚀 Guía Rápida - Flask CRUD API

## 📋 Requisitos Previos
- **Python 3.6+** instalado en tu sistema
- **pip** (viene incluido con Python)

## 🔧 Instalación

### 1. Crear el proyecto
```bash
# Crear directorio del proyecto
mkdir flask-crud-api
cd flask-crud-api

# Crear el archivo app.py (copiar el código del artefact anterior)
```

### 2. Instalar Flask
```bash
# Instalar Flask
pip install flask

# O si usas Python 3 específicamente:
pip3 install flask
```

### 3. (Opcional) Crear entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar Flask en el entorno virtual
pip install flask
```

## ▶️ Ejecución

### Ejecutar el servidor
```bash
# Desde el directorio del proyecto
python app.py

# O si usas Python 3:
python3 app.py
```

### ✅ Verificar que funciona
El servidor se iniciará en `http://localhost:5000`

Verás este mensaje:
```
🚀 Servidor Flask iniciando...
📍 Endpoints disponibles:
   GET    /info
   GET    /usuarios
   ...
```

## 🧪 Pruebas Rápidas

### Usando curl (terminal)
```bash
# Ver información del servidor
curl http://localhost:5000/info

# Listar usuarios
curl http://localhost:5000/usuarios

# Crear usuario
curl -X POST -H "Content-Type: application/json" \
  -d '{"nombre":"Ana","email":"ana@email.com"}' \
  http://localhost:5000/usuarios
```

### Usando navegador
- Abre `http://localhost:5000/info` en tu navegador
- O `http://localhost:5000/usuarios` para ver los usuarios

## 🛑 Detener el servidor
- Presiona `Ctrl + C` en la terminal donde está ejecutándose

## 📂 Estructura del proyecto
```
flask-crud-api/
├── app.py          # Tu aplicación Flask
└── venv/           # (opcional) Entorno virtual
```

## 🔍 Solución de Problemas

**Error: "Flask no encontrado"**
```bash
pip install flask
```

**Error: "Puerto ocupado"**
- Cambiar el puerto en `app.py`: `app.run(port=5001)`

**Error: "Python no encontrado"**
- Verificar instalación de Python: `python --version`