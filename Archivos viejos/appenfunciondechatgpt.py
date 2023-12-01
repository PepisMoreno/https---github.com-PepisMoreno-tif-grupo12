from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://://root:root@localhost:3306/plantasdb'#probar luego con plantas_bd
db = SQLAlchemy(app)
