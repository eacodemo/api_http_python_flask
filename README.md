# Api Rest 
## Python con Flask

## Requisitos
* Python
* Flask
* Postman o navegador
* Db browaser for Sqlite (Si requiere ver las tablas) u otro.

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
 
## Utilizar

* Para obtener todos los registros de los usuarios, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/user</code></li>
  </ul>
* Para obtener un registros especifico de un usuario, con el metodo <code>GET</code>
  <ul>
    <li> <code>http://localhost:5000/user/id</code></li>
  </ul>
  
* Para crear un nuevo usuario, con el metodo <code>POST</code>
  <ul>
    <li> <code>http://localhost:5000/user</code></li>
  </ul>

<ul>
    <li>Abre Postman y crea una nueva solicitud.</li>
    <li>Selecciona el método POST en la barra desplegable.</li>
    <li>Ingresa la URL a la que deseas enviar la solicitud en la barra de direcciones.</li>
    <li>Ve a la sección "Body" dentro de la solicitud en Postman.</li>
    <li>Selecciona <code>raw</code> como el tipo de datos.</li>
    <li>
        <pre>
{
  "nombreUsuario": "Juan Jose",
  "email": "Juan@gmail.com",
  "password": "fses",
  "tipo": "Gerente"
}
        </pre>
    </li>
</ul>
 
* Para actualizar los registros de los usuarios, con el metodo <code>PUT</code>
  <ul>
    <li> <code>http://localhost:5000/user/id</code></li>
  </ul>

* Para eliminar elregistro de un usuario, con el metodo <code>DELETE</code>
  <ul>
    <li> <code>http://localhost:5000/user/id</code></li>
  </ul>

