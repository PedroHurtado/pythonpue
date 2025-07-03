# Entornos Virtuales con Python (venv)

## ¿Qué es un entorno virtual?

Un entorno virtual es un espacio aislado donde puedes instalar paquetes de Python específicos para un proyecto sin afectar la instalación global de Python.

## Crear un entorno virtual

### En Windows

```bash
# Crear el entorno
python -m venv mi_entorno

# Activar el entorno
mi_entorno\Scripts\activate

# Desactivar el entorno
deactivate
```

### En Linux/Mac

```bash
# Crear el entorno
python3 -m venv mi_entorno

# Activar el entorno
source mi_entorno/bin/activate

# Desactivar el entorno
deactivate
```

## Comandos útiles

### Verificar que el entorno está activo
```bash
# Debería mostrar la ruta del entorno virtual
which python
```

### Instalar paquetes en el entorno
```bash
# Activar primero el entorno, luego instalar
pip install nombre_del_paquete
```

### Listar paquetes instalados
```bash
pip list
```

### Guardar dependencias
```bash
pip freeze > requirements.txt
```

### Instalar desde requirements.txt
```bash
pip install -r requirements.txt
```

## Ejemplo completo

```bash
# 1. Crear entorno para un proyecto
python -m venv mi_proyecto

# 2. Activar entorno
# Windows:
mi_proyecto\Scripts\activate
# Linux/Mac:
source mi_proyecto/bin/activate

# 3. Instalar paquetes
pip install requests flask

# 4. Guardar dependencias
pip freeze > requirements.txt

# 5. Trabajar en tu proyecto...

# 6. Desactivar cuando termines
deactivate
```

## Notas importantes

- **Siempre activa el entorno** antes de trabajar en tu proyecto
- **Un entorno por proyecto** para evitar conflictos
- **No versiones la carpeta del entorno** (añádela al `.gitignore`)
- **Usa `requirements.txt`** para compartir dependencias

## Estructura típica de proyecto

```
mi_proyecto/
├── mi_entorno/          # Entorno virtual (no versionar)
├── src/                 # Código fuente
├── requirements.txt     # Dependencias
├── README.md
└── .gitignore
```

## Contenido del .gitignore

```
# Entorno virtual
mi_entorno/
venv/
env/
```