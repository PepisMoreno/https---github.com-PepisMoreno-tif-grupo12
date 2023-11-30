from flask import Flask, render_template, jsonify, request
#request sirve para recolectar la data que viene del formulario
#jsonify para convertir archivos a json y viceversa.
from flask_cors import CORS
import sqlalchemy #ver si me funciona con esto.... no dice qué cuestión particular de esa librería, pero al menos deja correr el app py ocn flask..
import pymysql #ESTE ME LO DEJó instalar, veamos si sirve..
"""este no venía con este archivo pero lo puse en reemplazo del sqlalchemy, que no me dejaba utilizar""" 
#cors: recursos de origen cruzado
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
#esto supuestamente hace de nexo entre front y back

"""qué hay que hacer ahora:
1- configurar URI de la bsae de datos con el driver de Mysql, usuario, contraseña y nombre de la base de datos. 
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@host:3306/Plantas_db PEPIS: no sé si es esta la ruta, lo busqué en el chat gpt y por deducción maso entiendo esto..
2- de esto no entendí muy bien por qué: confgurar el seguimiento de modificaciones de sqlalchemy a false para mejora rendimiento.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False"""
# Crea una instancia de la clase SQLAlchemy y la asigna al objeto db para interactuar con la base de datos
#db = sqlalchemy(app) PEPIS: sigue sin dejarme usar, me rompe todo cuando lo pongo sin el # :(
# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)
"""faltan algunas partes que las copio acá pero que claramente hay que modificar en función de nuestra base de datos y nuestros parámetros:



"""
#Y esto de acá también es copiado del tutorial, habría que fijarse para trasladarlo a los argumentos específicos que maneja nuestra tabla:
"""@app.route("/productos", methods=["GET"])
def get_Productos():
    """
#    Endpoint para obtener todos los productos de la base de datos.

#    Retorna un JSON con todos los registros de la tabla de productos.

"""    all_productos = Producto.query.all()  # Obtiene todos los registros de la tabla de productos
    result = productos_schema.dump(all_productos)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla

'''
El código que sigue a continuación termina de resolver la API de gestión de productos, a continuación se destaca los principales detalles de cada endpoint, incluyendo su funcionalidad y el tipo de respuesta que se espera.
Endpoints de la API de gestión de productos:
get_producto(id):
    # Obtiene un producto específico de la base de datos
    # Retorna un JSON con la información del producto correspondiente al ID proporcionado
delete_producto(id):
    # Elimina un producto de la base de datos
    # Retorna un JSON con el registro eliminado del producto correspondiente al ID proporcionado
create_producto():
    # Crea un nuevo producto en la base de datos
    # Lee los datos proporcionados en formato JSON por el cliente y crea un nuevo registro de producto
    # Retorna un JSON con el nuevo producto creado
update_producto(id):
    # Actualiza un producto existente en la base de datos
    # Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del producto con el ID especificado
    # Retorna un JSON con el producto actualizado

'''
@app.route("/productos/<id>", methods=["GET"])
def get_producto(id):
    """
#    Endpoint para obtener un producto específico de la base de datos.

#    Retorna un JSON con la información del producto correspondiente al ID proporcionado.

"""producto = Producto.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    return producto_schema.jsonify(producto)  # Retorna el JSON del producto

@app.route("/productos/<id>", methods=["DELETE"])
def delete_producto(id):
    """
#    Endpoint para eliminar un producto de la base de datos.

#    Elimina el producto correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.

"""    producto = Producto.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    db.session.delete(producto)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return producto_schema.jsonify(producto)  # Retorna el JSON del producto eliminado

@app.route("/productos", methods=["POST"])  # Endpoint para crear un producto
def create_producto():
    """
#    Endpoint para crear un nuevo producto en la base de datos.

#    Lee los datos proporcionados en formato JSON por el cliente y crea un nuevo registro de producto en la base de datos.
#    Retorna un JSON con el nuevo producto creado.
    
"""nombre = request.json["nombre"]  # Obtiene el nombre del producto del JSON proporcionado
    precio = request.json["precio"]  # Obtiene el precio del producto del JSON proporcionado
    stock = request.json["stock"]  # Obtiene el stock del producto del JSON proporcionado
    imagen = request.json["imagen"]  # Obtiene la imagen del producto del JSON proporcionado
    new_producto = Producto(nombre, precio, stock, imagen)  # Crea un nuevo objeto Producto con los datos proporcionados
    db.session.add(new_producto)  # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return producto_schema.jsonify(new_producto)  # Retorna el JSON del nuevo producto creado

@app.route("/productos/<id>", methods=["PUT"])  # Endpoint para actualizar un producto
def update_producto(id):
    """
#    Endpoint para actualizar un producto existente en la base de datos.

#    Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del producto con el ID especificado.
#    Retorna un JSON con el producto actualizado.
    
"""producto = Producto.query.get(id)  # Obtiene el producto existente con el ID especificado

    # Actualiza los atributos del producto con los datos proporcionados en el JSON
    producto.nombre = request.json["nombre"]
    producto.precio = request.json["precio"]
    producto.stock = request.json["stock"]
    producto.imagen = request.json["imagen"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return producto_schema.jsonify(producto)  # Retorna el JSON del producto actualizado

'''
Este código es el programa principal de la aplicación Flask. Se verifica si el archivo actual está siendo ejecutado directamente y no importado como módulo. Luego, se inicia el servidor Flask en el puerto 5000 con el modo de depuración habilitado. Esto permite ejecutar la aplicación y realizar pruebas mientras se muestra información adicional de depuración en caso de errores.

'''
# Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)
"""

#---------------------------------RETOMAMOS NUESTRA APP.PY A PARTIR DE ACA-----------------------------------
"""@app.route("/Plantas", methods=["GET"])
def get_Plantas():
    all_plantas = plantas.query.all()  # Obtiene todos los registros de la tabla de productos
    result = plantas_schema.dump(all_plantas)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla"""

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
#ver cómo hacer para que app.py también te pueda derivar a la html agregador_plantas_desde_usuario.html

