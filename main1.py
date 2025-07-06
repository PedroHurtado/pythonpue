from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Simulamos una base de datos en memoria
usuarios = {}
next_id = 1

# Middleware para logging de requests
@app.before_request
def log_request():
    print(f"[{request.method}] {request.url}")

# Manejador de error 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Recurso no encontrado',
        'status_code': 404,
        'path': request.path
    }), 404

# Manejador de error 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'error': 'Solicitud incorrecta',
        'status_code': 400,
        'message': str(error)
    }), 400

# Manejador de error 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Error interno del servidor',
        'status_code': 500,
        'message': 'Algo salió mal en el servidor'
    }), 500

# GET - Obtener usuario por ID o listar todos
@app.route('/usuarios', methods=['GET'])
@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_usuarios(user_id=None):
    try:
        # Capturar datos del path
        path_info = {
            'endpoint': request.endpoint,
            'path': request.path,
            'user_id': user_id
        }
        
        # Capturar headers relevantes
        headers_info = {
            'content_type': request.headers.get('Content-Type'),
            'user_agent': request.headers.get('User-Agent'),
            'authorization': request.headers.get('Authorization'),
            'custom_header': request.headers.get('X-Custom-Header')
        }
        
        # Capturar query string parameters
        query_params = {
            'limit': request.args.get('limit', type=int),
            'format': request.args.get('format', 'json'),
            'filter': request.args.get('filter'),
            'all_params': dict(request.args)
        }
        
        if user_id:
            # Obtener usuario específico
            if user_id not in usuarios:
                return jsonify({
                    'error': 'Usuario no encontrado',
                    'user_id': user_id,
                    'status_code': 404
                }), 404
            
            usuario = usuarios[user_id]
            return jsonify({
                'status': 'success',
                'data': usuario,
                'request_info': {
                    'path': path_info,
                    'headers': headers_info,
                    'query_params': query_params
                }
            }), 200
        else:
            # Listar todos los usuarios
            usuarios_list = list(usuarios.values())
            
            # Aplicar limit si se especifica
            if query_params['limit']:
                usuarios_list = usuarios_list[:query_params['limit']]
            
            return jsonify({
                'status': 'success',
                'count': len(usuarios_list),
                'data': usuarios_list,
                'request_info': {
                    'path': path_info,
                    'headers': headers_info,
                    'query_params': query_params
                }
            }), 200
            
    except Exception as e:
        return jsonify({
            'error': 'Error procesando la solicitud GET',
            'message': str(e),
            'status_code': 500
        }), 500

# POST - Crear nuevo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    try:
        global next_id
        
        # Capturar datos del path
        path_info = {
            'endpoint': request.endpoint,
            'path': request.path,
            'method': request.method
        }
        
        # Capturar headers
        headers_info = {
            'content_type': request.headers.get('Content-Type'),
            'content_length': request.headers.get('Content-Length'),
            'authorization': request.headers.get('Authorization'),
            'api_key': request.headers.get('X-API-Key')
        }
        
        # Capturar query string
        query_params = dict(request.args)
        
        # Capturar body
        if not request.is_json:
            return jsonify({
                'error': 'Content-Type debe ser application/json',
                'received_content_type': request.headers.get('Content-Type'),
                'status_code': 400
            }), 400
        
        body_data = request.get_json()
        
        # Validar datos requeridos
        if not body_data or 'nombre' not in body_data:
            return jsonify({
                'error': 'Faltan datos requeridos',
                'required_fields': ['nombre'],
                'received_data': body_data,
                'status_code': 400
            }), 400
        
        # Crear usuario
        nuevo_usuario = {
            'id': next_id,
            'nombre': body_data['nombre'],
            'email': body_data.get('email'),
            'edad': body_data.get('edad'),
            'created_at': 'now'
        }
        
        usuarios[next_id] = nuevo_usuario
        next_id += 1
        
        return jsonify({
            'status': 'created',
            'message': 'Usuario creado exitosamente',
            'data': nuevo_usuario,
            'request_info': {
                'path': path_info,
                'headers': headers_info,
                'query_params': query_params,
                'body': body_data
            }
        }), 201
        
    except json.JSONDecodeError:
        return jsonify({
            'error': 'JSON inválido en el body',
            'status_code': 400
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Error procesando la solicitud POST',
            'message': str(e),
            'status_code': 500
        }), 500

# PUT - Actualizar usuario completo
@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def update_usuario(user_id):
    try:
        # Capturar datos del path
        path_info = {
            'endpoint': request.endpoint,
            'path': request.path,
            'user_id': user_id,
            'method': request.method
        }
        
        # Capturar headers
        headers_info = {
            'content_type': request.headers.get('Content-Type'),
            'if_match': request.headers.get('If-Match'),
            'authorization': request.headers.get('Authorization')
        }
        
        # Capturar query string
        query_params = {
            'force': request.args.get('force', 'false').lower() == 'true',
            'validate': request.args.get('validate', 'true').lower() == 'true',
            'all_params': dict(request.args)
        }
        
        # Verificar que el usuario existe
        if user_id not in usuarios:
            return jsonify({
                'error': 'Usuario no encontrado para actualizar',
                'user_id': user_id,
                'status_code': 404
            }), 404
        
        # Capturar y validar body
        if not request.is_json:
            return jsonify({
                'error': 'Content-Type debe ser application/json',
                'status_code': 400
            }), 400
        
        body_data = request.get_json()
        
        if not body_data or 'nombre' not in body_data:
            return jsonify({
                'error': 'Datos insuficientes para actualización completa',
                'required_fields': ['nombre'],
                'status_code': 400
            }), 400
        
        # Actualizar usuario (PUT reemplaza completamente)
        usuario_anterior = usuarios[user_id].copy()
        usuarios[user_id] = {
            'id': user_id,
            'nombre': body_data['nombre'],
            'email': body_data.get('email'),
            'edad': body_data.get('edad'),
            'updated_at': 'now'
        }
        
        return jsonify({
            'status': 'updated',
            'message': 'Usuario actualizado exitosamente',
            'data': usuarios[user_id],
            'previous_data': usuario_anterior,
            'request_info': {
                'path': path_info,
                'headers': headers_info,
                'query_params': query_params,
                'body': body_data
            }
        }), 200
        
    except json.JSONDecodeError:
        return jsonify({
            'error': 'JSON inválido en el body',
            'status_code': 400
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'Error procesando la solicitud PUT',
            'message': str(e),
            'status_code': 500
        }), 500

# DELETE - Eliminar usuario
@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def delete_usuario(user_id):
    try:
        # Capturar datos del path
        path_info = {
            'endpoint': request.endpoint,
            'path': request.path,
            'user_id': user_id,
            'method': request.method
        }
        
        # Capturar headers
        headers_info = {
            'authorization': request.headers.get('Authorization'),
            'confirm_delete': request.headers.get('X-Confirm-Delete'),
            'cascade': request.headers.get('X-Cascade-Delete')
        }
        
        # Capturar query string
        query_params = {
            'force': request.args.get('force', 'false').lower() == 'true',
            'backup': request.args.get('backup', 'true').lower() == 'true',
            'reason': request.args.get('reason'),
            'all_params': dict(request.args)
        }
        
        # Verificar que el usuario existe
        if user_id not in usuarios:
            return jsonify({
                'error': 'Usuario no encontrado para eliminar',
                'user_id': user_id,
                'status_code': 404
            }), 404
        
        # Capturar datos del usuario antes de eliminar
        usuario_eliminado = usuarios[user_id].copy()
        
        # Verificar confirmación si se requiere
        if not query_params['force'] and headers_info['confirm_delete'] != 'true':
            return jsonify({
                'warning': 'Eliminación requiere confirmación',
                'message': 'Incluye header X-Confirm-Delete: true o query param force=true',
                'user_to_delete': usuario_eliminado,
                'status_code': 409
            }), 409
        
        # Eliminar usuario
        del usuarios[user_id]
        
        return jsonify({
            'status': 'deleted',
            'message': 'Usuario eliminado exitosamente',
            'deleted_data': usuario_eliminado,
            'remaining_users': len(usuarios),
            'request_info': {
                'path': path_info,
                'headers': headers_info,
                'query_params': query_params
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error procesando la solicitud DELETE',
            'message': str(e),
            'status_code': 500
        }), 500

# Ruta adicional para probar captura de múltiples parámetros del path
@app.route('/api/v1/usuarios/<int:user_id>/posts/<int:post_id>', methods=['GET'])
def get_user_post(user_id, post_id):
    try:
        path_info = {
            'user_id': user_id,
            'post_id': post_id,
            'full_path': request.path,
            'endpoint': request.endpoint
        }
        
        return jsonify({
            'status': 'success',
            'message': 'Ejemplo de múltiples parámetros en path',
            'path_params': path_info,
            'headers': dict(request.headers),
            'query_params': dict(request.args)
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error en ruta con múltiples parámetros',
            'message': str(e),
            'status_code': 500
        }), 500

# Ruta de información del servidor
@app.route('/info', methods=['GET'])
def server_info():
    return jsonify({
        'server': 'Flask Mini CRUD API',
        'version': '1.0.0',
        'endpoints': {
            'GET /usuarios': 'Listar todos los usuarios',
            'GET /usuarios/<id>': 'Obtener usuario específico',
            'POST /usuarios': 'Crear nuevo usuario',
            'PUT /usuarios/<id>': 'Actualizar usuario completo',
            'DELETE /usuarios/<id>': 'Eliminar usuario',
            'GET /api/v1/usuarios/<user_id>/posts/<post_id>': 'Ejemplo múltiples path params'
        },
        'total_users': len(usuarios)
    }), 200

if __name__ == '__main__':
    # Crear algunos usuarios de ejemplo
    usuarios[1] = {'id': 1, 'nombre': 'Juan Pérez', 'email': 'juan@email.com', 'edad': 30}
    usuarios[2] = {'id': 2, 'nombre': 'María García', 'email': 'maria@email.com', 'edad': 25}
    next_id = 3
    
    print("🚀 Servidor Flask iniciando...")
    print("📍 Endpoints disponibles:")
    print("   GET    /info")
    print("   GET    /usuarios")
    print("   GET    /usuarios/<id>")
    print("   POST   /usuarios")
    print("   PUT    /usuarios/<id>")
    print("   DELETE /usuarios/<id>")
    print("   GET    /api/v1/usuarios/<user_id>/posts/<post_id>")
    
    app.run(debug=True, host='0.0.0.0', port=5000)