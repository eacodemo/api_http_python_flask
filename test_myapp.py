import unittest
from flask import Flask
from myapp import app, db  
from models import User, Proyecto, AsociacionProyectoUsuario, HistoriaUsuario, Tarea
from flask import (
  Flask, request, jsonify)

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

    def test_get_specific_user(self):
        user = User(nombreUsuario='TestUser', email='test@example.com', password='password', tipo='admin')
        db.session.add(user)
        db.session.commit()

        response = self.app.get(f'/usuario/{user.id}')
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        user_data = {
            'nombreUsuario': 'TestUser',
            'email': 'test@example.com',
            'password': 'password',
            'tipo': 'admin'
        }

        response = self.app.post('/usuario', json=user_data)
        self.assertEqual(response.status_code, 200)  # 
       

    def test_update_user(self):
        user = User(nombreUsuario='TestUser', email='test@example.com', password='password', tipo='admin')
        db.session.add(user)
        db.session.commit()

        updated_data = {
            'nombreUsuario': 'UpdatedUser',
            'email': 'updated@example.com',
            'password': 'updated_password',
            'tipo': 'updated'
        }

        response = self.app.put(f'/usuario/{user.id}', data=updated_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        user = User(nombreUsuario='TestUser', email='test@example.com', password='password', tipo='admin')
        db.session.add(user)
        db.session.commit()

        response = self.app.delete(f'/usuario/{user.id}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
