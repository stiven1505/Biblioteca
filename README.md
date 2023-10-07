# Biblioteca
Aplicacion para la gestion de biblioteca, creado con django y sqlite, donde habran dos roles uno como administrador que sera el unico rol para crear libros y los demas usuarios tendran funciones como pedir prestado libros, devolverlos, listar los que ese usuario tiene en su poder y los que ha tenido (manejo de historial) 

## Instalación

1. Clona el repositorio: `git clone https://github.com/tu_usuario/tu_proyecto.git`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual: `source venv/bin/activate` (en sistemas Unix)
4. Configura las variables de entorno: `cp .env.example .env`
5. Ejecuta las migraciones de la base de datos: `python manage.py migrate`

## Uso

1. Inicia el servidor de desarrollo: `python manage.py runserver`
2. Abre tu navegador web y accede a `http://localhost:8000` para ver la aplicación en funcionamiento.
