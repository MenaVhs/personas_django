# Notas personales
para correr el servidor<br>
python .\manage.py runserver<br>

------------------ crearApp nombreApp <br>
python .\manage.py startapp webapp <br>

archivo __init__ no debe cambiar, para indicar que es un paquete de Python
archivo views.py se agrega el código para el navegador web
Registrar la app: capeta sap>settings.py<br>
    en installed_apps, se agregan las aplicaciones web, en este caso webapp <br>

archivo urls.py: mapeo de urls, ahí se agregan las rutas a las que se puede acceder desde la webapp.
se debe agregar en el archivo de views.py dentro de la carpteta de la app (webserver)

OJO! Indicar la ruta del código fuente, con Mark Directory as > Sources Root <br>

### Conexión con la Base de Datos DE PostgreSQL
1. Agregar databases 
2. En sap > settigs.py
   3. buscar DATABASES <br>
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sap_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
   ```
   4. Instalar conector hacia PostgreSQL <br>
   ```python -m pip install psycopg2```

### Migraciones
En el archivo de setting.py, ya hay aplicaciones instaladas como app de admin,
estas aplicaciones se configurar en la BD. 

si se corre el servidor, puede mandar el siguiente mensaje
"You have 18 unapplied migration(s)." <br>

correr: ```python manage.py showmigrations```

### sincronización con la BD
````python .\manage.py migrate
````