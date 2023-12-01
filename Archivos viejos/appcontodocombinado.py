# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request, render_template
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
# Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow

import mysql.connector 
import pymysql

app = Flask(__name__)
CORS = app

# Configura la URI de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/proyecto"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/plantasdb"
# Configura el seguimiento de modificaciones de SQLAlchemy a False para mejorar el rendimiento
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Crea una instancia de la clase SQLAlchemy y la asigna al objeto db para interactuar con la base de datos
db = SQLAlchemy(app)
# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)

class Planta(db.Model):  # Producto hereda de db.Model
    def __init__(self, id, nombre_comun, nombre_cientifico): #,luz, riego, suelo, ubicacion, interior_o_exterior):
        self.id = id
        self.nombre_comun = nombre_comun
        self.nombre_cientifico = nombre_cientifico
        """self.luz = luz
        self.riego = riego
        self.suelo = suelo
        self.ubicacion = ubicacion
        self.interior_o_exterior= interior_o_exterior"""

with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos

# Definición del esquema para la clase Producto
class PlantaSchema(ma.Schema):
    """
    Esquema de la clase Producto.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Producto.
    """
    class Meta:
        fields = ("id", "nombre_comun", "nombre_cientifico")

planta_schema = PlantaSchema()  # Objeto para serializar/deserializar un producto
plantas_schema = PlantaSchema(many=True)  # Objeto para serializar/deserializar múltiples productos

@app.route("/plantas", methods=["GET"])
def get_Plantas():
    all_plantas = Planta.query.all()  # Obtiene todos los registros de la tabla de productos
    result = plantas_schema.dump(all_plantas)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla

@app.route("/plantas/<id>", methods=["GET"])
def get_planta(id):
    planta= Planta.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    return planta_schema.jsonify(planta)  # Retorna el JSON del producto

@app.route("/plantas/<id>", methods=["DELETE"])
def delete_planta(id):
    planta = Planta.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    db.session.delete(planta)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return planta_schema.jsonify(planta)  # Retorna el JSON del producto eliminado

@app.route("/plantas", methods=["POST"])  # Endpoint para crear un producto
def create_planta():
    nombre_comun = request.json["nombre_comun"]  # Obtiene el nombre del producto del JSON proporcionado
    nombre_cientifico = request.json["nombre_cientifico"]  # Obtiene el precio del producto del JSON proporcionado
    #luz = request.json["luz"]  # Obtiene el stock del producto del JSON proporcionado
    #riego = request.json["riego"]  # Obtiene la imagen del producto del JSON proporcionado
    #suelo = request.json["suelo"]
    #ubicacion = request.json ["ubicacion"]
    #interior_o_exterior = request.json ["interior_o_exterior"]
    new_planta = Planta(nombre_comun, nombre_cientifico)#, luz, riego, suelo, ubicacion, interior_o_exterior)  # Crea un nuevo objeto Producto con los datos proporcionados
    db.session.add(new_planta)  # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return planta_schema.jsonify(new_planta)  # Retorna el JSON del nuevo producto creado

@app.route("/plantas/<id>", methods=["PUT"])  # Endpoint para actualizar un producto
def update_planta(id):
    planta = Planta.query.get(id)  # Obtiene el producto existente con el ID especificado

     # Actualiza los atributos del producto con los datos proporcionados en el JSON
    planta.nombre_comun = request.json["nombre_comun"]
    planta.nombre_cientifico = request.json["nombre_cientifico"]
    #planta.luz = request.json["luz"]
    #planta.riego = request.json["riego"]
    #planta.suelo = request.json["suelo"]
    #planta.ubicacion = request.json["ubicacion"]
    #planta.interior_o_exterior = request.json["interior o exterior"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return planta_schema.jsonify(planta)  # Retorna el JSON del producto actualizado

if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)