import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# define sqlite database file path 
db_dir = os.path.abspath('data.sqlite')

# app Configuracion 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin'
app.config["DEBUG"] = True

# Conexion para base de datos linux
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+db_dir+'?check_same_thread=False'

# Conexion para base de datos windows
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_dir
db = SQLAlchemy(app)
