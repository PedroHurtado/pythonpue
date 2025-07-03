from flask import Flask,send_from_directory,jsonify

app = Flask(__name__)



@app.after_request
def add_custom_header(response):
    # Se ejecutará después de cada petición
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
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

if __name__ == '__main__':
    app.run(debug=True)