# Proyecto Python

Proyecto Python con estructura y orquestación con **setuptools** utilizado de base en los proyectos de Dyopem.

Implementa una calculadora con una interfaz web/rest en la que ejecutar las operaciones disponibles junto a una 
prueba de conexión a Big Data para lectura/escritura y visualización de un gráficos.

#### 1. Estructura

Estructura de directorios y ficheros del proyecto:

Directorio                      | Contenido
--------------------------------|----------------
**proyecto**                    | Código del paquete
proyecto/**api**                | Código para generar un API WEB/REST
proyecto/**ops**                | Código para las diferentes operaciones que puede ejecutar el paquete
proyecto/**static**             | Contenido estático parte web (imágenes, hojas de estilo, librerías, etc.)
proyecto/**templates**          | Plantillas parte web: páginas HTML (Templates Flask - Jinja2)
proyecto/**templates**/auth     | Páginas HTML para seguridad WEB (login)
proyecto/**templates**/errors   | Páginas HTML para errores
proyecto/**templates**/flasgger | Páginas HTML para personalización de documentación REST (Swagger)
proyecto/**templates**/pages    | Páginas HTML para interfaz WEB
**tests**                       | Pruebas (unitarias, integración, etc.)
docs                            | Documentación (manuales, documentación técnica, etc.)
extras                          | Otros (ficheros de datos, etc.)
scripts                         | Scripts (scripts ejecución, creación de objetos en BD, etc.)

Fichero                       | Utilidad
------------------------------|----------------------------------
proyecto/**\_\_init\_\_.py** | Inicialización (configuración, logs, base de datos, etc.)
proyecto/**\_\_main\_\_.py** | Punto de entrada principal para la ejecución de la aplicación.
proyecto/api/web.py          | Encargada de definir e implementar la interfaz web del proyecto. Autenticación por credenciales corporativas (login). Importante: las credenciales se bloquean (intervalo 30 mins) en caso de ser incorrectas.
proyecto/api/rest.py         | Encargada de definir e implementar la interfaz rest del proyecto. Autenticación por credenciales corporativas (op login). Importante: las credenciales se bloquean (intervalo 30 mins) en caso de ser incorrectas.
proyecto/api/client.py       | Ejemplo de cliente interfaz REST con autenticación por token JWT.

Fichero              | Utilidad
---------------------|----------------------------------
**README.md**        | Descripción del proyecto/repositorio
**MANIFEST.in**      | Ficheros/carpetas a incluir al generar paquete
**requirements.txt** | Dependencias del proyecto
**setup.py**         | Configuración del proyecto en formato **setuptools**
.gitignore           | Ficheros/carpetas ignoradas en el repositorio GIT

#### 2. Dependencias

En el fichero **requirements.txt** se definen las dependencias del proyecto:

Paquete    | Utilidad
-----------|----------------------------------
setuptools | Gestión de paquetes
nose       | Ejecución automática de pruebas
nose2      | Ejecución automática de pruebas
coverage   | Análisis de cobertura de pruebas
pylint     | Análisis de calidad de código
bandit     | Análisis de calidad de código
flake8     | Análisis de calidad de código
wheel      | Empaquetado y distribución
twine      | Empaquetado y distribución
pycco      | Generación de documentación

Paquete    | Utilidad
-----------|----------------------------------
numpy      | Soporte para vectores y matrices
pandas     | Manipulación y análisis de datos
matplotlib | Generación de gráficos

Paquete            | Utilidad
-------------------|----------------------------------
Werkzeug           | Librería de aplicaciones web WSGI
Flask              | Framework para crear aplicaciones web
Flask-Login        | Extensión en Flask para añadir control de usuarios/sesión WEB
Flask-RESTfu       | Extensión en Flask para añadir soporte REST
Flask-JWT-Extended | Extensión en Flask para añadir control de acceso en REST con token JWT
Flask-Cors         | Extensión en Flask para añadir control CORS a peticiones
flasgger           | Librería para documentar la interfaz REST con herramienta Swagger
bravado            | Librería para generar un cliente en Python a partir de un API REST documentado con Swagger

Paquete          | Utilidad
-----------------|----------------------------------
**dyopemutils**  | Librería utilidades Dyopem.
**dyopemseg**    | Librería seguridad Dyopem.

La librería **dyopemutils** contiene las clases de configuración interna/externa mediante fichero YAML, logs separados (debug|info|warning|error) con salida a consola|fichero con rotado y conexión|consultas a Big Data utilizando Kerberos.
La librería **dyopemseg** contiene toda la lógica para implantar una capa de seguridad a las interfaces WEB (Auth) y REST (JWT).

Las dependencias se pueden instalar en local ejecutando el comando:

    pip install -r requirements.txt

Al distribuir el código en formato paquete Python, al instalarlo con PIP se instalarán de forma automática las dependencias definidas en el fichero **requirements.txt** e incorporadas en la definición **setup.py**.

#### 3. Paquete

La configuración para utilizar la herramienta _setuptools_ se define en el fichero _setup.py_.
Parámetros importantes:

    name: nombre del paquete.

    python_requires: versión requerida de Python.

    version: versión del paquete en formato Semver (https://semver.org/) siendo la inicial la 1.0.0
    
    description: Descripción simple del proyecto.

    long_description: Descripción ampliada del proyecto. Se obtiene a partir del fichero README.md

    url: Url de Confluence del proyecto.

Importante:

- El campo versión es necesario modificarlo de forma manual en el proceso de generación de release del paquete y es necesario que la versión esté alineada a la rama. Ejemplo: en la rama _release/1.1.0_ el valor de versión debe ser _1.1.0_.
- El fichero README.md del repositorio/producto debe tener la información más relavante del proyecto. Ejemplo: descripción, parámetros de configuración, ejecución, etc.

Configuración de la aplicación:

- En el fichero **\_\_init\_\_.py** se definen los parámetros de configuración por defecto en las variables **app_def** y **log_def**.
- Utilizando los objetos 'config' y 'log' se pueden acceder a los parámetros de configuración en el resto de la aplicación y guardar información de log en los ficheros de log.
- Los valores de configuración de aplicación/log se pueden sobrescribir cargando un fichero de configuración YAML que se encontrará en las siguientes rutas:
  - /home/usuario/nombre-del-paquete/nombre-del-paquete.yml
  - ./nombre-del-paquete.yml
- De forma alternativa se puede añadir una ruta diferente del fichero YAML (ejemplo: ruta en DataLab) asignando la variable **path_alt** en el fichero **\_\_init\_\_.py** en la inicialización de la configuración.

- Ejemplo de fichero YAML de configuración:

        app:
          titulo: PROYECTO
          host: 'gtaa-cloudera.awselb.enelint.global'
          port: 21050
          odbc_dsn: 'impala_endesa'
          cadena: 'PROYECTO CALCULADORA'
          entero: 5
          flotante: 10.0
          booleano: True
        log:
          mode: file
          level: debug
          count: 100
          path: /userdata/proyecto/proyecto_logs

- Configuración del log:

        mode: console|file|null
        level: debug|info|warning|error
        size: tamaño en bytes para rotar
        count: cantidad de ficheros de log a mantener
        formatter: formato utilizado
        formatter_web: formato utilizado en web
        formatter_datefmt: formato fechas
        color: distinción de tipo de logs por colores (console).
        path: ruta en la que guardar los logs

Los comandos que se pueden ejecutar en **setuptools** son los siguientes:

- Build:

    `python setup.py build`

- Test:

    `python setup.py test`

- Install:

    `python setup.py install`

- Dist:

    `python setup.py sdist bdist_wheel`

- Documentación:

    `pycco -i -p proyecto/* tests/* -d docs/proyecto`

- Clean:

    `python setup.py clean`

#### 4. Ejecución

Ejecución de la aplicación:

- Utilizando el fichero **\_\_main\_\_.py**:

        python -m proyecto

- Utilizando otros puntos de entrada/ficheros:

        python -m proyecto.ops.funciones
        python -m proyecto.ops.ecuaciones

- Iniciar la interfaz web/rest (http://localhost:8080/ y http://localhost:8090/):

        python -m proyecto.ui
        python -m proyecto.api.web
        python -m proyecto.api.rest

- Iniciar la interfaz web/rest con servidor uWSGI (Web Server Gateway Interface):

        pip install uwsgi
        
        uwsgi --socket 0.0.0.0:8080 --protocol=http --enable-threads --module proyecto.api.wsgi.web:app
        uwsgi --socket 0.0.0.0:8090 --protocol=http --enable-threads --module proyecto.api.wsgi.rest:app
