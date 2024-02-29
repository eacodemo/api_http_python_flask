from flask import (
  Flask, request, jsonify)
from settings import db, app
from models import User
from models import Proyecto
from models import AsociacionProyectoUsuario
from models import HistoriaUsuario
from models import Tarea

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


@app.route('/asociacionproyectousuario', methods=['GET'])
def get_all_asociacionproyectousuario():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = AsociacionProyectoUsuario.query.with_entities(
            AsociacionProyectoUsuario.id, AsociacionProyectoUsuario.idProyecto,
            AsociacionProyectoUsuario.idUsuario, AsociacionProyectoUsuario.rol
        ).all()
        message.update({
            'status': 200,
            'message': 'Se recuperan TODOS los registros de AsociacionProyectoUsuario',
            'data': data
        })
    except:
        pass
    return jsonify(message)

@app.route('/asociacionproyectousuario/<int:id>', methods=['GET'])
def get_specific_asociacionproyectousuario(id):
    message = {
        'status': 404,
        'message': 'AsociacionProyectoUsuario no existe'
    }
    data = AsociacionProyectoUsuario.query.with_entities(
        AsociacionProyectoUsuario.id, AsociacionProyectoUsuario.idProyecto,
        AsociacionProyectoUsuario.idUsuario, AsociacionProyectoUsuario.rol
    ).filter_by(id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
        'status': 200,
        'message': 'Se recupero el registro de AsociacionProyectoUsuario',
        'data': data
    })
    return jsonify(message)

@app.route('/asociacionproyectousuario', methods=['POST'])
def create_asociacionproyectousuario():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = request.get_json()

        idProyecto = data.get('idProyecto', '')
        idUsuario = data.get('idUsuario', '')
        rol = data.get('rol', '')

        asociacionproyectousuario = AsociacionProyectoUsuario(
            idProyecto=idProyecto,
            idUsuario=idUsuario,
            rol=rol
        )
        db.session.add(asociacionproyectousuario)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'AsociacionProyectoUsuario creado exitosamente!!! ',
            'asociacion_proyecto_usuario_id': asociacionproyectousuario.id
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/asociacionproyectousuario/<int:id>', methods=['PUT'])
def update_asociacionproyectousuario(id):
    message = {
        'status': 404,
        'message': 'AsociacionProyectoUsuario no encontrado'
    }
    try:
        new_id_proyecto = request.form.get('idProyecto', None)
        new_id_usuario = request.form.get('idUsuario', None)
        new_rol = request.form.get('rol', None)
        
        try:
            current_asociacion_proyecto_usuario = AsociacionProyectoUsuario.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_id_proyecto:
            current_asociacion_proyecto_usuario.idProyecto = new_id_proyecto
        if new_id_usuario:
            current_asociacion_proyecto_usuario.idUsuario = new_id_usuario
        if new_rol:
            current_asociacion_proyecto_usuario.rol = new_rol

        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Detalles de AsociacionProyectoUsuario actualizados exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/asociacionproyectousuario/<int:id>', methods=['DELETE'])
def delete_asociacionproyectousuario(id):
    message = {
        'status': 404,
        'message': 'AsociacionProyectoUsuario no encontrado'
    }
    try:
        current_asociacion_proyecto_usuario = AsociacionProyectoUsuario.query.get_or_404(id)
        db.session.delete(current_asociacion_proyecto_usuario)
        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Registro de AsociacionProyectoUsuario eliminado exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp



@app.route('/historiausuario', methods=['GET'])
def get_all_historias():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = HistoriaUsuario.query.with_entities(
            HistoriaUsuario.id, HistoriaUsuario.Detalles,
            HistoriaUsuario.CriteriosAceptacion, HistoriaUsuario.Estado,
            HistoriaUsuario.IdProyecto, HistoriaUsuario.IdTarea
        ).all()
        message.update({
            'status': 200,
            'message': 'Se recuperan TODOS los registros de HistoriaUsuario',
            'data': data
        })
    except:
        pass
    return jsonify(message)

@app.route('/historiausuario/<int:id>', methods=['GET'])
def get_specific_historia(id):
    message = {
        'status': 404,
        'message': 'Historia de usuario no existe'
    }
    data = HistoriaUsuario.query.with_entities(
        HistoriaUsuario.id, HistoriaUsuario.Detalles,
        HistoriaUsuario.CriteriosAceptacion, HistoriaUsuario.Estado,
        HistoriaUsuario.IdProyecto, HistoriaUsuario.IdTarea
    ).filter_by(id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
        'status': 200,
        'message': 'Se recupero el registro de Historia de usuario',
        'data': data
    })
    return jsonify(message)

@app.route('/historiausuario', methods=['POST'])
def create_historia_usuario():
    try:
        data = request.get_json()

        detalles = data.get('Detalles', '')
        criterios_aceptacion = data.get('CriteriosAceptacion', '')
        estado = data.get('Estado', '')
        id_proyecto = data.get('IdProyecto', None)
        id_tarea = data.get('IdTarea', None)

        historia_usuario = HistoriaUsuario(
            Detalles=detalles,
            CriteriosAceptacion=criterios_aceptacion,
            Estado=estado,
            IdProyecto=id_proyecto,
            IdTarea=id_tarea
        )

        db.session.add(historia_usuario)
        db.session.commit()

        message = {
            'status': 201,
            'message': 'Historia de Usuario creada exitosamente!!! ',
            'historia_usuario_id': historia_usuario.id
        }
    except Exception as e:
        message = {
            'status': 404,
            'message': f'Algo salió mal: {str(e)}'
        }

    resp = jsonify(message)
    return resp


@app.route('/historiausuario/<int:id>', methods=['PUT'])
def update_historia(id):
    message = {
        'status': 404,
        'message': 'Historia de usuario no encontrada'
    }
    try:
        new_detalles = request.form.get('Detalles', None)
        new_criterios_aceptacion = request.form.get('CriteriosAceptacion', None)
        new_estado = request.form.get('Estado', None)
        new_id_proyecto = request.form.get('IdProyecto', None)
        new_id_tarea = request.form.get('IdTarea', None)

        try:
            current_historia = HistoriaUsuario.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_detalles:
            current_historia.Detalles = new_detalles
        if new_criterios_aceptacion:
            current_historia.CriteriosAceptacion = new_criterios_aceptacion
        if new_estado:
            current_historia.Estado = new_estado
        if new_id_proyecto:
            current_historia.IdProyecto = new_id_proyecto
        if new_id_tarea:
            current_historia.IdTarea = new_id_tarea

        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Detalles de Historia de usuario actualizados exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/historiausuario/<int:id>', methods=['DELETE'])
def delete_historia(id):
    message = {
        'status': 404,
        'message': 'Historia de usuario no encontrada'
    }
    try:
        current_historia = HistoriaUsuario.query.get_or_404(id)
        db.session.delete(current_historia)
        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Registro de Historia de usuario eliminado exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/tarea', methods=['GET'])
def get_all_tareas():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = Tarea.query.with_entities(
            Tarea.id, Tarea.descripcion,
            Tarea.estado, Tarea.idHistoriaUsuario
        ).all()
        message.update({
            'status': 200,
            'message': 'Se recuperan TODOS los registros de Tarea',
            'data': data
        })
    except:
        pass
    return jsonify(message)

@app.route('/tarea/<int:id>', methods=['GET'])
def get_specific_tarea(id):
    message = {
        'status': 404,
        'message': 'Tarea no existe'
    }
    data = Tarea.query.with_entities(
        Tarea.id, Tarea.descripcion,
        Tarea.estado, Tarea.idHistoriaUsuario
    ).filter_by(id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
        'status': 200,
        'message': 'Se recupero el registro de Tarea',
        'data': data
    })
    return jsonify(message)

@app.route('/tarea', methods=['POST'])
def create_tarea():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = request.get_json()

        descripcion = data.get('Descripcion', '')
        estado = data.get('Estado', '')
        id_historia_usuario = data.get('IdHistoriaUsuario', '')

        tarea = Tarea(
            Descripcion=descripcion,
            Estado=estado,
            IdHistoriaUsuario=id_historia_usuario
        )
        db.session.add(tarea)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'Tarea creada exitosamente!!! ',
            'tarea_id': tarea.id
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/tarea/<int:id>', methods=['PUT'])
def update_tarea(id):
    message = {
        'status': 404,
        'message': 'Tarea no encontrada'
    }
    try:
        new_descripcion = request.form.get('Descripcion', None)
        new_estado = request.form.get('Estado', None)
        new_id_historia_usuario = request.form.get('IdHistoriaUsuario', None)

        try:
            current_tarea = Tarea.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_descripcion:
            current_tarea.Descripcion = new_descripcion
        if new_estado:
            current_tarea.Estado = new_estado
        if new_id_historia_usuario:
            current_tarea.IdHistoriaUsuario = new_id_historia_usuario

        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Detalles de Tarea actualizados exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp

@app.route('/tarea/<int:id>', methods=['DELETE'])
def delete_tarea(id):
    message = {
        'status': 404,
        'message': 'Tarea no encontrada'
    }
    try:
        current_tarea = Tarea.query.get_or_404(id)
        db.session.delete(current_tarea)
        db.session.commit()
        message.update({
            'status': 200,
            'message': 'Registro de Tarea eliminado exitosamente!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


 # Se encuentra activada el modo DEBUG
if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", debug=True)



