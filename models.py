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
        return self.id + self.nombreUsuario + self.email + self.tipo

