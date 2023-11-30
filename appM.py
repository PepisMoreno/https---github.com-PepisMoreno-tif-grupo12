from flask import Flask, jsonify, render_template, request
import pymysql 
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)  # crear el objeto app de la clase Flask

CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

#----------------decorador, me lleva al index cuando hago la petición http
@app.route("/")
def index():
    return render_template("index.html")

#----------------creamos otro decorador, para q el usuario ingrese info a la BD
@app.route("/agregador") #declaramos la ruta /agregador
def agregador(): #en esta función vamos a recibir la info que recolectamos en el formulario
    return render_template("agregador.html")


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:salas887@localhost/plantas_bd'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# defino los modelos de la base de datos y tabla
class Planta(db.Model):   # la clase Planta hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre_comun=db.Column(db.String(100))
    nombre_cientifico=db.Column(db.Integer)
    foto=db.Column(db.String(400))

#crea el  constructor de la clase (id porque lo crea sola mysql por ser auto_incremento)
    def __init__(self,nombre_comun, nombre_cientifico, foto):   
        self.nombre_comun=nombre_comun   
        self.nombre_cientifico=nombre_cientifico
        self.foto=foto

    #  si hay que crear la otra tabla sería..
    #def __init__(self,iluminacion, riego, ubicacion, suelo, plaga):   
    #        self.iluminacion=iluminacion   
    #        self.riego=riego
    #        self.ubicacion=ubicacion
    #        self.suelo=suelo
    #        self.plaga=plaga

#with app.app_context():
#    db.create_all()  # aqui crea todas las tablas
#
#Campos en tabla
class PlantaSchema(ma.Schema):
    class Meta:
        fields=('id','nombre_comun','nombre_científico','foto')




planta_schema=PlantaSchema()            # El objeto plantaschema es para traer un producto
plantas_schema=PlantaSchema(many=True)  # El objeto planta_schema es para traer multiples registros de producto



#----------------------GET-OBTENER-------------------
# crea los endpoint o rutas (json)
@app.route('/plantas',methods=['GET'])
def get_Plantas():
    all_plantas=Planta.query.all()         # el metodo query.all() lo hereda de db.Model
    result=plantas_schema.dump(all_plantas)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/plantas/<id>',methods=['GET'])
def get_planta(id):
    planta=Planta.query.get(id)
    return planta_schema.jsonify(planta)   # retorna el JSON de un producto recibido como parametro



#--------------------DELETE-ELIMINAR------------------------

@app.route('/plantas/<id>',methods=['DELETE'])
def delete_planta(id):
    planta=Planta.query.get(id)
    db.session.delete(planta)
    db.session.commit()
    return planta_schema.jsonify(planta)   # me devuelve un json con el registro eliminado

#-----------------POST-CREAR-------------------------
@app.route('/plantas', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre_comun=request.json['nombre_comun']
    nombre_cientifico=request.json['nombre_cientifico']
    foto=request.files['foto']
     #Guardamos la imagen en el servidor
    filename = secure_filename(foto.filename)
    foto.save(filename)

    new_planta=Planta(nombre_comun,nombre_cientifico,foto)
    db.session.add(new_planta)
    db.session.commit()
    return planta_schema.jsonify(new_planta)

#--------------------PUT-ACTUALIZAR------------------------
@app.route('/plantas/<id>' ,methods=['PUT'])
def update_planta(id):
    planta=Planta.query.get(id)
 
    nombre_comun=request.json['nombre_comun']
    nombre_cientifico=request.json['nombre_cientifico']
    foto=request.json['foto']


    planta.nombre_comun=nombre_comun
    planta.nombre_cientifico=nombre_cientifico
    planta.foto=foto


    db.session.commit()
    return planta_schema.jsonify(planta)
 


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000

