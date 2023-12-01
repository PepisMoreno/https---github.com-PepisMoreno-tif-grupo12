from flask import Flask, jsonify, render_template, request
import pymysql 
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



#importo librería para conectar con una BD, con flaskext no me funcionó
#request sirve para recolectar la data que viene del formulario

#instanciamos las clases. Flask 1°
app = Flask(__name__)


#decorador, me lleva al index cuando hago la petición http
@app.route("/")
def index():
    return render_template("index.html")

#-----------LLAMADO DE SQL-----------
def conexion():
    return pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           db="plantas_bd")

cursor=conexion.cursor() 

try:
    with open ("plantas_bd.sql","r") as plantas_bd_sql:
        consulta_sql=plantas_bd_sql.read()
    cursor.execute(consulta_sql)
    conexion.commit()

    

    print("consulta exitosa")
except Exception as e:
    print(f"Error: {e} .ntente buscar de nuevo.")
finally:
    cursor.close()
    conexion.close()


#creamos otro decorador, para q el usuario ingrese info a la BD
@app.route("/agregador") #declaramos la ruta /agregador
def agregador(): #en esta función vamos a recibir la info que recolectamos en el formulario
    return render_template("agregador.html")

#----------------------GET-OBTENER-------------------
@app.route("/store", methods=["GET"]) 
def obtener_plantas():
    try:
        cursor=conexion.cursor(dictionary=True)
        cursor.execute("SELECT FROM plantas")
        resultados=cursor.fetchall()
    
        return jsonify({'plantas':resultados})

    except Exception as e:
        return jsonify({'error':{e}})


#Debe haber 2: uno que me muestre todos y uno por ID
@app.route("/store/<int:id>", methods=["GET"])
def obtener_planta_id(id):
    
    try:
        cursor=conexion.cursor(dictionary=True)
        consulta_sql= "SELECT FROM plantas WHERE id=%s"
        cursor.execute(consulta_sql,(id))
        
        resultado=cursor.fetchone()

        if resultado:   
            return jsonify({'plantas':resultado})
        else:
            return jsonify({'No encontramos la planta que indicaste. Agregala!'})

    except Exception as e:
        return jsonify({'Error:':{e}})

#-----------------POST-CREAR-------------------------
@app.route("/store", methods=["POST"]) 
def store():
    #print(request.form). request.form contiene el json que envió el cliente
    nombrePlanta = request.form('nom')
    nombrecient = request.form('nomcient')
    fotoplanta = request.files('nomfoto')
#Guardamos la imagen en el servidor
    filename = secure_filename(fotoplanta.filename)
    fotoplanta.save(filename)

    #Conexión a la base de datos
    conn= pymysql.connect()
    cursor= conn.cursor()

    #Insertamos datos a la bd
    sql= "INSERT INTO plantas (nombre_comun, nombre_científico, foto) VALUES (%s, %s, %s)";
    datos=(nombrePlanta,nombrecient,fotoplanta.filename)
    
    cursor.execute(sql, datos)
    conn.commit()
    #Cerramos la conexión
    cursor.close()
    conn.close() 

    return render_template("index.html")

#@app.route() #completar acá la ruta
#def consulta():
 #   nombrePlanta = request.form('Nombre')
  #  consulta = request.form('consulta')
    #acá iria algo para usar esa data que me mando el usuario y buscar en la BD la respuesta que saldrá por ouput
   # output= print("buenas")#acá va la respuesta que le damos al usuario, a su consulta. sacada de la BD no se como
    #return #podriamos hacer con un if else, si el usuario pregunto por la luz o el agua o etc, le damos tal o cual respuesta.

#--------------------PUT-ACTUALIZAR------------------------
@app.route("/store/<int:id>", methods=["PUT"])
def actualizar_planta(id):
    planta= (id)
    if request.is_json:
        data=request.json

        nombrePlanta = data.get['nom']
        nombrecient = data.get['nomcient']
        fotoplanta = data.get['nomfoto']

        #Conexión a la base de datos
        conn= pymysql.connect()
        cursor= conn.cursor()

        #Insertamos datos a la bd
        sql= "INSERT INTO plantas (nombre_comun, nombre_científico, foto, id) VALUES (%s, %s, %s,%s)"
        datos=(nombrePlanta,nombrecient,fotoplanta.filename, id)
        
        cursor.execute(sql, datos)
        conn.commit()
        #Cerramos la conexión
        cursor.close()
        conn.close() 

        return render_template("index.html")
    else:
        return "La solicitud no contiene datos JSON", 400    

#--------------------DELETE-ELIMINAR------------------------
@app.route("/delete/<int:id>", methods=["DELETE"])
def store(id):
    nombrePlanta = request.form['nom']
    nombrecient = request.form['nomcient']
    fotoplanta = request.files*['nomfoto']
    


#----------------Programa ppal -----------------------
if __name__=="__main__":
    app.run(debug=True)
    #ejecuta el servidor Flask en el puerto 5000