import mysql.connector
# Conexión a la base de datos MySQL
conn = mysql.connector.connect (host='localhost', user='root', password='root', database='plantasdb', port= '3306')

print(conn)