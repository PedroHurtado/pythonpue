from flask import Flask,send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static","index.html")

@app.route("/about")
def about():
    return "<h1>Acerca de nosotros<h1>"

if __name__ == '__main__':
    app.run(debug=True)