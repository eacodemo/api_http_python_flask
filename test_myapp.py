import unittest
from flask import Flask
from myapp import app, db  # Asegúrate de ajustar según tu estructura de archivos y nombres
from models import User, Proyecto, AsociacionProyectoUsuario, HistoriaUsuario, Tarea


class MyAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_users(self):
        response = self.app.get('/usuario')
        self.assertEqual(response.status_code, 200)
        # Aquí puedes agregar más aserciones según tu lógica

    def test_get_specific_user(self):
        user = User(nombreUsuario='TestUser', email='test@example.com', password='password', tipo='admin')
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f'/usuario/{user.id}')
        self.assertEqual(response.status_code, 200)
        # Otras aserciones según tu lógica

    # Agrega más pruebas para otras funciones

if __name__ == '__main__':
    unittest.main()
