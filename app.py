from flask import Flask, render_template, request
import pymysql
from werkzeug.utils import secure_filename


#importo librería para conectar con una BD, con flaskext no me funcionó
#request sirve para recolectar la data que viene del formulario

#instanciamos las clases. Flask 1°
app = Flask(__name__)


#decorador, me lleva al index cuando hago la petición http
@app.route("/")
def index():
    return render_template("index.html")

def obtener_conexion():
    return pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           db="plantas_bd")

#creamos otro decorador, para q el usuario ingrese info a la BD
@app.route("/agregador") #declaramos la ruta /agregador
def agregador(): #en esta función vamos a recibir la info que recolectamos en el formulario
    return render_template("agregador.html")

#----------------------GET--------------------
@app.route("/store/<id>", methods=["GET"]) 
def listaplanta():
   try: 
        cursor = conexion.connection.cursor()
            sql= "INSERT INTO plantas (nombre_comun, nombre_científico, foto) VALUES (%s, %s, %s)"
            datos=(nombrePlanta,nombrecient,fotoplanta.filename)      cursor.execute(sql)

            plantas = []
            for fila in datos:
                planta = {'nombre_comun':fila[0], 'nombre_científico':fila[1], 'foto':fila[2]}
                plantas.append(plantas)
            return jsonify({'Nombre':"nombrecomun", 'Nombre científico':"nombre_científico"})
        except Exception as ex:
            return jsonify({'Mensaje':"No existe"})

#    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
#    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
#    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla
#--------------------POST-------------------------
#Crea ruta para almacenar los datos enviados en el form
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

#--------------------PUT-------------------------
@app.route("/store/<int:id>", methods=["PUT"])
def store(id):
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

#--------------------DELETE-------------------------
@app.route("/delete/<int:id>", methods=["DELETE"])
def store(id):
    nombrePlanta = request.form['nom']
    nombrecient = request.form['nomcient']
    fotoplanta = request.files*['nomfoto']
    


#----------------Programa ppal -----------------------
if __name__=="__main__":
    app.run(debug=True)
    #ejecuta el servidor Flask en el puerto 5000