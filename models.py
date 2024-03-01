from settings import db
from sqlalchemy import Column, Integer, Text
from datetime import datetime

# Definición del modelo de Usuario
class User(db.Model,):
    def get_id(self):
        return str(self.id)
    
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

# Definición del modelo de Proyecto
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



# Definición del modelo de AsociacionProyectoUsuario
class AsociacionProyectoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return self.idProyecto + self.idUsuario + self.rol
    

# Definición del modelo de HistoriaUsuario
class HistoriaUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Detalles = db.Column(db.Text)
    CriteriosAceptacion = db.Column(db.Text)
    Estado = db.Column(db.String(50), nullable=False)
    IdProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    IdTarea = db.Column(db.Integer, db.ForeignKey('tarea.id'))

    def __str__(self):
        return self.Detalles + self.CriteriosAceptacion + self.Estado + self.IdProyecto + self.IdTarea
    

# Definición del modelo de Tarea
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(50), nullable=False)
    idHistoriaUsuario = db.Column(db.Integer, db.ForeignKey('historia_usuario.id'))

    def __str__(self):
        return self.descripcion + self.estado + str(self.idHistoriaUsuario)
 