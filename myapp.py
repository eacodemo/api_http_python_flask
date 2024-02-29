from flask import (
  Flask, request, jsonify)
from settings import db, app
from models import User
from models import Proyecto


@app.route('/usuario', methods=['GET'])
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


@app.route('/usuario/<int:id>', methods=['GET'])
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
      'message': 'Se recupero el registro',
      'data': data
    })
    return jsonify(message)


@app.route('/usuario', methods=['POST'])
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
        data = request.get_json()

        nombreUsuario = data.get('nombreUsuario', '')
        email = data.get('email', '')
        password = data.get('password', '')
        tipo = data.get('tipo', '')

        user = User(
          nombreUsuario=nombreUsuario,
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


@app.route('/usuario/<int:id>', methods=['PUT'])
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
        new_name = request.form.get('nombreUsuario', None)
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
            current_user.nombreUsuario = new_name
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


@app.route('/usuario/<int:id>', methods=['DELETE'])
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

@app.route('/proyecto', methods=['GET'])
def get_all_proyectos():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = Proyecto.query.with_entities(
            Proyecto.id, Proyecto.nombre,
            Proyecto.descripcion, Proyecto.fechaInicio
        ).all()
        message.update({
            'status': 200,
            'message': 'Se recuperan TODOS los registros de proyectos',
            'data': data
        })
    except:
        pass
    return jsonify(message)

@app.route('/proyecto/<int:id>', methods=['GET'])
def get_specific_proyecto(id):
    message = {
        'status': 404,
        'message': 'Proyecto no encontrado'
    }
    data = Proyecto.query.with_entities(
        Proyecto.id, Proyecto.nombre,
        Proyecto.descripcion, Proyecto.fechaInicio
    ).filter_by(id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
        'status': 200,
        'message': 'Se recupero el registro del proyecto',
        'data': data
    })
    return jsonify(message)

@app.route('/proyecto', methods=['POST'])
def create_proyecto():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = request.get_json()

        nombre = data.get('nombre', '')
        descripcion = data.get('descripcion', '')
      

        proyecto = Proyecto(
            nombre=nombre,
            descripcion=descripcion,
        )
        db.session.add(proyecto)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'Proyecto creado exitosamente!!! ',
            'proyecto_id': proyecto.id
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/proyecto/<int:id>', methods=['PUT'])
def update_proyecto(id):
    message = {
        'status': 404,
        'message': 'Proyecto no encontrado'
    }
    try:
        new_nombre = request.form.get('nombre', None)
        new_descripcion = request.form.get('descripcion', None)
        new_fechaInicio = request.form.get('fechaInicio', None)

        current_proyecto = Proyecto.query.get_or_404(id)

        if new_nombre:
            current_proyecto.nombre = new_nombre
        if new_descripcion:
            current_proyecto.descripcion = new_descripcion
        if new_fechaInicio:
            current_proyecto.fechaInicio = new_fechaInicio

        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Detalles del proyecto actualizados exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/proyecto/<int:id>', methods=['DELETE'])
def delete_proyecto(id):
    message = {
        'status': 404,
        'message': 'Proyecto no encontrado'
    }
    try:
        current_proyecto = Proyecto.query.get_or_404(id)
        db.session.delete(current_proyecto)
        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Registro del proyecto eliminado exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp

 # Se encuentra activada el modo DEBUG
if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", debug=True)



