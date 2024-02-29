from settings import db
from sqlalchemy import Column, Integer, Text
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(60) )
    email = db.Column(db.String(60))
    password = db.Column(db.String(500))
    tipo = db.Column(db.String(300))
    create_at = db.Column(
        db.TIMESTAMP,
        default=datetime.utcnow,
        nullable=False
      )

    def __str__(self):
        return self.nombreUsuario + self.email + self.tipo

class Proyecto(db.Model):
    
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(255))
  descripcion = db.Column(db.Text)
  fechaInicio = db.Column(
     db.TIMESTAMP, 
     nullable=False, 
     default=datetime.utcnow)

  def __str__(self):
    return self.nombre + self.descripcion + self.fechaInicio
  

class AsociacionProyectoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return self.idProyecto + self.idUsuario + self.rol