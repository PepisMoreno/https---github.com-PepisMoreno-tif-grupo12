from flask import Flask, render_template, request
#request sirve para recolectar la data que viene del formulario

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
