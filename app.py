from flask import Flask, render_template, request
import pymysql
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


@app.route("/store", methods=["POST"])
def store():
    nombrePlanta = request.form('nom')
    nombrecient = request.form('nomcient')
    fotoplanta = request.files('nomfoto')

    sql= "INSERT INTO plantas (nombre_comun, nombre_científico, foto) VALUES (%S, %S, %S)";
    datos=(nombrePlanta,nombrecient,fotoplanta.filename)
    conn= pymysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return render_template("index.html")

#@app.route() #completar acá la ruta
#def consulta():
 #   nombrePlanta = request.form('Nombre')
  #  consulta = request.form('consulta')
    #acá iria algo para usar esa data que me mando el usuario y buscar en la BD la respuesta que saldrá por ouput
   # output= print("buenas")#acá va la respuesta que le damos al usuario, a su consulta. sacada de la BD no se como
    #return #podriamos hacer con un if else, si el usuario pregunto por la luz o el agua o etc, le damos tal o cual respuesta.


if __name__=="__main__":
    app.run(debug=True)