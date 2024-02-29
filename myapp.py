from flask import (
  Flask, request, jsonify)
from settings import db, app
from models import User


@app.route('/user', methods=['GET'])
def get_all_users():
    """
    esta función está asignada con el punto final /usuario y
    representa todos los registros de usuario utilizando el método GET Http
    """
    message = {
      'status': 404,
      'message': 'Algo salió mal'
    }
    try:
        data = User.query.with_entities(
          User.id, User.nombreUsuario,
          User.email, User.tipo,
          User.password).all()
        message.update({
          'status': 200,
          'message': 'Se recuperan TODOS los registros',
          'data': data
        })
    except:
        pass
    return jsonify(message)


@app.route('/user/<int:id>', methods=['GET'])
def get_specific_user(id):
    """
    esta función está asignada con el punto final /user/pk y
    Representa registros de usuario específicos con respecto a su pk.
    usando el método GET Http
    """    
    message = {
      'status': 404,
      'message': 'Usuario no existe'
    }
    data = User.query.with_entities(
      User.id, User.nombreUsuario,
      User.email, User.tipo,
      User.password).filter_by(id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
      'status': 200,
      'message': 'Algo salio mal',
      'data': data
    })
    return jsonify(message)


@app.route('/user', methods=['POST'])
def create_user():
    """
    esta función está asignada con el punto final /usuario y
    crea registros de usuario utilizando el método POST Http
    """    
    message = {
      'status': 404,
      'message': 'Algo salió mal'
      }
    try:
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        tipo = request.form.get('tipo', '')
        user = User(
          name=name,
          email=email,
          password=password,
          tipo=tipo
        )
        db.session.add(user)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'Usuario creado exitosamente!!! ',
            'user_id': user.id
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    """
    esta función está asignada con el punto final /user/pk y
    actualiza registros de usuarios específicos utilizando el método PUT Http
    """  
    message = {
      'status': 404,
      'message': 'Usuario no encontrado'
    }
    try:
        new_name = request.form.get('name', None)
        new_email = request.form.get('email', None)
        new_password = request.form.get('password', None)
        new_tipo = request.form.get('tipo', None)
        try:
            current_user = User.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_email:
            current_user.email = new_email
        if new_name:
            current_user.name = new_name
        if new_password:
            current_user.password = new_password
        if new_tipo:
            current_user.tipo = new_tipo

        db.session.commit()
        message.update({
          'status': 200,
          'message': 'Detalles del usuario actualizados exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    esta función está asignada con el punto final /user/pk y
    elimina registros de usuarios específicos utilizando el método DELETE Http
    """  
    message = {
      'status': 404,
      'message': 'Usuario no encontrado'
    }
    try:
        current_user = User.query.get_or_404(id)
        db.session.delete(current_user)
        db.session.commit()
        message.update({
          'status': 200,
          'message': 'registro de usuario eliminado exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", debug=True)



