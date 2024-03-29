# Api Rest 
## Python con Flask

## Requisitos
* Python
* Flask
* Postman o navegador
* Db browaser for Sqlite (Si requiere ver las tablas) u otro.
## Documentacion

* Toda la documentacion se encuentra en los archivos *.py

## Como utilizar este codigo
* Clonar el repositorio
  <ul>
    <li><code>git clone https://github.com/eacodemo/api_http_python_flask.git</code></li>
  </ul>

* Instalar dependencias 
  <ul>
    <li><code>pip install -r requerimientos.txt</code></li>
  </ul>

* Arrancar o ejecutar el codigo
  <ul>
    <li><code> python myapp.py </code></li>
    <li><code> python3 myapp.py </code></li>
  </ul>

## Arrancar los Test Unitarios

* Arrancar o ejecutar el codigo
  <ul>
    <li><code> python test_myapp.py </code></li>
    <li><code> python3 test_myapp.py </code></li>
  </ul>

 
## Utilizar los metodos de CRUD para este proyecto

### Usuarios

* Para obtener todos los registros de los usuarios, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/usuario</code></li>
  </ul>
* Para obtener un registros especifico de un usuario, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/usuario/id</code></li>
  </ul>
  
* Para crear un nuevo usuario, con el metodo <code>POST</code>
  <ul>
    <li> <code>http://localhost:5000/usuario</code></li>
  </ul>

  <ul>
    <li>Abre Postman y crea una nueva solicitud.</li>
    <li>Selecciona el método <code>POST</code> en la barra desplegable.</li>
    <li>Ingresa la URL a la que deseas enviar la solicitud en la barra de direcciones.</li>
    <li>Ve a la sección "Body" dentro de la solicitud en Postman.</li>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    {
      "nombreUsuario": "Juan Jose",
      "email": "Juan@gmail.com",
      "password": "fses",
      "tipo": "Gerente"
    }	
        </pre> </ul>
 
* Para actualizar los registros de los usuarios, con el metodo <code>PUT</code>
  <ul>
    <li> <code>http://localhost:5000/usuario/id</code></li>
  </ul>
  <ul>
    <li>Abre Postman y crea una nueva solicitud.</li>
    <li>Selecciona el método <code>PUT</code> en la barra desplegable.</li>
    <li>Ingresa la URL a la que deseas enviar la solicitud en la barra de direcciones.</li>
    <li>Ve a la sección "Body" dentro de la solicitud en Postman.</li>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    {
        "nombreUsuario": "Juan Jose",
        "email": "Juan@gmail.com",
        "password": "igndsfuigfr", 
        "tipo": "Gerente"
    }
        </pre> </ul>


* Para eliminar elregistro de un usuario, con el metodo <code>DELETE</code>
  <ul>
    <li> <code>http://localhost:5000/usuario/id</code></li>
  </ul>

### Proyectos

* Para obtener todos los registros de los proyectos, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/proyecto</code></li>
  </ul>
* Para obtener un registros especifico de un proyecto, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/proyecto/id</code></li>
  </ul>
  
* Para crear un nuevo proyecto, con el metodo <code>POST</code>
  <ul>
    <li> <code>http://localhost:5000/proyecto</code></li>
  </ul>

  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    {
      "nombre": "Proyecto Nuevo 5",
      "descripcion": "Descripción del Proyecto 5"
    }
        </pre> </ul>
 
* Para actualizar los registros de los proyectos, con el metodo <code>PUT</code>
  <ul>
    <li> <code>http://localhost:5000/proyecto/id</code></li>
  </ul>
  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    {
        "nombre": "Proyecto Nuevo 5",
        "descripcion": "Descripción del Proyecto  - actualizar"
    }
       </pre> </ul>


* Para eliminar elregistro de un proyecto, con el metodo <code>DELETE</code>
  <ul>
    <li> <code>http://localhost:5000/proyecto/id</code></li>
  </ul>

### AsociacionProyectoUsuario

Para obtener todos los registros de los AsociacionProyectoUsuario, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/asociacionproyectousuario</code></li>
  </ul>
* Para obtener un registros especifico de un AsociacionProyectoUsuario, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/asociacionproyectousuario/id</code></li>
  </ul>
  
* Para crear una nueva asociasiondeproeyctousuario, con el metodo <code>POST</code>
  <ul>
    <li> <code>http://localhost:5000/asociacionproyectousuario</code></li>
  </ul>

  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    {
      "idProyecto": 1,
      "idUsuario": 2,
      "rol": "Gerente"
    }
        </pre>
 </ul>
 
* Para actualizar los registros de las asociaciones, con el metodo <code>PUT</code>
  <ul>
    <li> <code>http://localhost:5000/asociacionproyectousuario/id</code></li>
  </ul>
  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    {
        "idProyecto": 1,
        "idUsuario": 2,
        "rol": "Desarrollador"
    }
        </pre>
 </ul>


* Para eliminar elregistro de una asociacion, con el metodo <code>DELETE</code>
  <ul>
    <li> <code>http://localhost:5000/asociacionproyectousuario/id</code></li>
  </ul>

  
### Historia de usuario

Para obtener todos los registros de las historias de usuario, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/historiausuario</code></li>
  </ul>
* Para obtener un registro especifico de una historia de usuario, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/historiausuario/id</code></li>
  </ul>
  
* Para crear una nueva historia de usuario, con el metodo <code>POST</code>
  <ul>
    <li> <code>http://localhost:5000/historiausuario</code></li>
  </ul>

  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
 	{
	 "Detalles": "Detalles de la historia",
 	 "CriteriosAceptacion": "Criterios de aceptación",
 	 "Estado": "En progreso",
  	 "IdProyecto": 1,
 	 "IdTarea": 1
	}   
        </pre>
  </ul>
 
* Para actualizar los registros de las historias de usuario, con el metodo <code>PUT</code>
  <ul>
    <li> <code>http://localhost:5000/historiausuario/id</code></li>
  </ul>
  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    	 {
         "Detalles": "Detalles de la historia",
         "CriteriosAceptacion": "Criterios de aceptación",
         "Estado": "En progreso",
         "IdProyecto": 1,
         "IdTarea": 1
        }
        </pre>
  </ul>

* Para eliminar el registro de una historia de usuario, con el metodo <code>DELETE</code>
  <ul>
    <li> <code>http://localhost:5000/historiausuario/id</code></li>
  </ul>
  
### Tareas

Para obtener todos los registros de las tareas, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/tarea</code></li>
  </ul>
* Para obtener un registro especifico de una tarea, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/tarea/id</code></li>
  </ul>
  
* Para crear una nueva tarea, con el metodo <code>POST</code>
  <ul>
    <li> <code>http://localhost:5000/tarea</code></li>
  </ul>

  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
    	{
	 "descripcion": "Tarea 4",
  	 "estado": "Nuevo",
  	 "idHistoriaUsuario": 3
	}
        </pre>
  </ul>
 
* Para actualizar los registros de las tareas, con el metodo <code>PUT</code>
  <ul>
    <li> <code>http://localhost:5000/tarea/id</code></li>
  </ul>
  <ul>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
        <pre>
        {
          "descripcion": "Tarea 4",
          "estado": "Nuevo",
          "idHistoriaUsuario": 2
        }
        </pre>
  </ul>

* Para eliminar elregistro de una tarea, con el metodo <code>DELETE</code>
  <ul>
    <li> <code>http://localhost:5000/tarea/id</code></li>
  </ul>
  


