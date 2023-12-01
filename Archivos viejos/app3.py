from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Reemplaza con tu usuario de MySQL
    password='root',  # Reemplaza con tu contraseña de MySQL
    database='plantasplantas',  # Reemplaza con el nombre de tu base de datos
    port= '3306'
)

cursor = conn.cursor()

# Rutas para operaciones CRUD

# Obtener todas las plantas
@app.route('/plantasplantas', methods=['GET'])
def get_plantas():
    cursor.execute('SELECT * FROM plantasplantas')
    rows = cursor.fetchall()
    plants = []
    for row in rows:
        plant = {
            'id': row[0],
            'nombre': row[1],
            'nombre_cientifico': row[2],
            'luz': row[3],
            'riego': row[4],
            'suelo': row[5],
            'ubicacion': row[6],
            'interior_o_exterior': row[7]
        }
        plants.append(plant)
    return jsonify({'plantas': plants})

# Crear una nueva planta
@app.route('/plantas', methods=['POST'])
def create_planta():
    new_plant = request.json
    query = '''INSERT INTO plantas 
                (nombre, nombre_cientifico, luz, riego, suelo, ubicacion, interior_o_exterior)
                VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    values = (new_plant['nombre'], new_plant['nombre_cientifico'], new_plant['luz'],
              new_plant['riego'], new_plant['suelo'], new_plant['ubicacion'], new_plant['interior_o_exterior'])
    cursor.execute(query, values)
    conn.commit()
    return jsonify({'message': 'Planta creada exitosamente'}), 201

# Actualizar una planta existente por ID
@app.route('/plantas/<int:plant_id>', methods=['PUT'])
def update_planta(plant_id):
    updated_plant = request.json
    query = '''UPDATE plantas SET 
                nombre=%s, nombre_cientifico=%s, luz=%s, riego=%s, suelo=%s, ubicacion=%s, interior_o_exterior=%s
                WHERE id=%s'''
    values = (updated_plant['nombre'], updated_plant['nombre_cientifico'], updated_plant['luz'],
              updated_plant['riego'], updated_plant['suelo'], updated_plant['ubicacion'],
              updated_plant['interior_o_exterior'], plant_id)
    cursor.execute(query, values)
    conn.commit()
    return jsonify({'message': f'Planta con ID {plant_id} actualizada exitosamente'})

# Eliminar una planta por ID
@app.route('/plantas/<int:plant_id>', methods=['DELETE'])
def delete_planta(plant_id):
    cursor.execute('DELETE FROM plantas WHERE id=%s', (plant_id,))
    conn.commit()
    return jsonify({'message': f'Planta con ID {plant_id} eliminada exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)