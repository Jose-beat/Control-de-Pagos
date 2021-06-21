# Control de Pagos Estudiantiles

_Este proyecto es una practica para la materia de **Desarrollo de Software** con la creacion de una aplicacion web basada en **Django** que permita la administracion de pagos, grados, alumnos, reportes y usuarios de una escuela._



### Instalación 🔧

_Vamos a comenzar clonando el proyecto con el siguiente comando._

_Clonamos el Proyecto_

```
$ git clone https://github.com/Jose-beat/Control-de-Pagos
```
**Nota: Verificar que la carpeta contenedora se llame 'Control_de_Pagos'**

_Despues vamos a instalar y crear un nuevo entorno virtual con:_

```
$ pip3 install virtualenv
$ virtualenv entornoControlPagos
```
_Ahora vamos a la carpeta de nuestro entorno y lo activamos_
```
$ source entornoControlPagos/bin/activate
```
_Instalaremos las siguientes librerias definidas en los comandos_
```
$ pip install django
$ pip freeze
$ pip install django-crispy-forms
```
_Volvemos a la carpeta de nuestro proyecto y generamos una migracion_
```
$ python3 manage.py  makemigrations
```
_Ahora vamos a ejecutar la migracion con un argumento de sincronizacion_
```
$ python3 manage.py migrate --run-syncdb
```
_Por ultimo vamos a ejecutar nuestros **Seeders** para meter algunos datos de forma automatica_
```
$ python3 manage.py loaddata alumnos_seeders
```
_Ahora ya podemos ejecutar nuestro servidor_
```
$ python3 manage.py runserver
```
_Por ultimo creamos un **Super Usuario** para acceder al sistema completo_

```
$ python3 manage.py createsuperuser
```

## Construido con 🛠️

_Esta aplicacion fue construida con las siguientes herramientas:_

* [Python 3.9](https://www.python.org/) - Lenguaje de programacion base para el proyecto
* [Pip](https://pypi.org/project/pip/) - Manejador de Dependencias
* [VirtualEnv](https://virtualenv.pypa.io/en/latest/) - Entorno virtual
* [Django](https://www.djangoproject.com/) - Framework para construir la aplicacion web
* [Pillow](https://pypi.org/project/Pillow/) - Libreria para subir imagenes al servidor
* [Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Libreria para el manejo de formularios en Django


## Versionado 📌

Usamos [Git](https://git-scm.com/) para el versionado local de la app y [GitHub](https://github.com) para el trabajo con versionado remoto y colaborativo.

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Jose Uriel Rodriguez Ramirez** - *Creacion del proyecto, Modulo de Alumnos, Grados e Interfaz* - [Jose-beat](https://github.com/Jose-beat)
* **Fatima Isabel Santiago Reynoso** - *Interfaz y modulo de Pagos* - [Fatima9007](https://github.com/Fatima9007)
* **Melissa Dominguez Guarneros** - *Documentación* - [Melissa8717-do](https://github.com/Melissa8717-do)
* **Miguel Sanchez Contreras** - *Sistema de Acceso* - [ayoy147](https://github.com/ayoy147)


---
Creditos y Saludos a _Andrés Villanueva_ - [Villanuevand](https://github.com/Villanuevand) 😊 Gracias por la Plantilla
