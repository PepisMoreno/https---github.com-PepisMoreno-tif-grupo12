from flask import Flask, render_template, jsonify, request
#request sirve para recolectar la data que viene del formulario
#jsonify para convertir archivos a json y viceversa.
from flask_cors import CORS
#from sqlalchemy import Sqlalchemy
#cors: recursos de origen cruzado
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
#esto supuestamente hace de nexo entre front y back

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
#ver cómo hacer para que app.py también te pueda derivar a la html agregador_plantas_desde_usuario.html
