import sys
import importlib.util
from pathlib import Path
from flask import Flask

sys.path.insert(0, str(Path('.').resolve()))

def cargar_modulos_y_blueprints(base_path: str, extension='.py'):
    base_path = Path(base_path)
    blueprints = []
    files = base_path.rglob(f'*{extension}')
    for py_file in files:
        if py_file.name == '__init__.py':
            continue

        modulo_relativo = py_file.relative_to(base_path).with_suffix('')
        modulo_nombre = '.'.join(modulo_relativo.parts)
        ruta_modulo = py_file.resolve()

        spec = importlib.util.spec_from_file_location(modulo_nombre, ruta_modulo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        # Si el módulo tiene un blueprint llamado `bp`, lo recogemos
        if hasattr(modulo, 'bp'):
            blueprints.append(modulo.bp)

    return blueprints

app = Flask(__name__)

# Cargar y registrar blueprints
blueprints = cargar_modulos_y_blueprints("app/features")
for bp in blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
