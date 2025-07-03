from flask import Flask,send_from_directory,jsonify,abort



app = Flask(__name__)

@app.errorhandler(404)
def error_handler_404(e):
    return jsonify({
        "message":"No existe el recurso"
    }),404

@app.errorhandler(Exception)
def error_handler_exceptions(e:Exception):
    return jsonify({
        "message":str(e),
        "code":500
    }),500
@app.after_request
def add_custom_header(response):
    # Se ejecutará después de cada petición
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    #quitar una cabecera
    response.headers.pop('Server', None)
    return response

@app.route("/")
def index():
    return send_from_directory("static","index.html")

@app.route("/about")
def about():
    data={
        "id":1,
        "name": "Pedro Hurtado"
    }
    return jsonify(data),201, {
        "X-App": "pyton"
    }

@app.route("/cursos/<int:id>")
def courses(id):
    if id!=1:
        #return abort(404)   
        #raise Exception("El registro no existe")
        abort(Exception("El registro no existe"))
    return jsonify({
        "id":id
    }),200

if __name__ == '__main__':
    app.run(debug=True)