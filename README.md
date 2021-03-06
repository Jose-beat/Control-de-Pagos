# Control de Pagos Estudiantiles

_Este proyecto es una practica para la materia de **Desarrollo de Software** con la creacion de una aplicacion web basada en **Django** que permita la administracion de pagos, grados, alumnos, reportes y usuarios de una escuela._




### Instalación local 🔧
![Azure-icon](res/icons/computer.png)

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
_Instalaremos las librerias en el archivo requirements.txt_
```
$ cd ..
$ cd Control_de_Pagos/
$ pip install -r requirements.txt
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
$ python3 manage.py loaddata user_seeders
$ python3 manage.py loaddata grados_seeders
$ python3 manage.py loaddata alumnos_seeders
```
_Por ultimo creamos un **Super Usuario** para acceder al sistema completo_

```
$ python3 manage.py createsuperuser
```

_Ahora ya podemos ejecutar nuestro servidor_
```
$ python3 manage.py runserver
```

## Construido con 🛠️

_Esta aplicacion fue construida con las siguientes herramientas:_

* [Python 3.9](https://www.python.org/) - Lenguaje de programacion base para el proyecto
* [Pip](https://pypi.org/project/pip/) - Manejador de Dependencias
* [VirtualEnv](https://virtualenv.pypa.io/en/latest/) - Entorno virtual
* [Django](https://www.djangoproject.com/) - Framework para construir la aplicacion web
* [Pillow](https://pypi.org/project/Pillow/) - Libreria para subir imagenes al servidor
* [Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Libreria para el manejo de formularios en Django

## Nota de Versiones ⏱
_Se describiran las versiones actuales y futuras para tener mejor perspectivas de los cambios:_
* [v0.0.1](https://github.com/Jose-beat/Control-de-Pagos/releases/tag/v0.0.1) - Version de Origen que contiene la fase mas basica de la aplicacion
* [v0.0.2](https://github.com/Jose-beat/Control-de-Pagos/releases/tag/v0.0.2) - Version con sidebar y navBar corregidos
* [v0.0.3](https://github.com/Jose-beat/Control-de-Pagos/releases/tag/v0.0.3) - Se añadieron Modulos a la aplicacion
* [v0.0.4](https://github.com/Jose-beat/Control-de-Pagos/releases/tag/v0.0.4) - Correccion Responsive de la aplicacion
* [v0.0.5](https://github.com/Jose-beat/Control-de-Pagos/releases/tag/v0.0.5) -  Cambios en la estructura de base de datos y algunos formularios, ademas de los seeders y la adicion del modulo que se encargara de registrar los pagos y deudas.
* [v0.1.0](https://github.com/Jose-beat/Control-de-Pagos/releases/tag/v0.1.0) - Se añadieron Mas usuarios. Por lo que ahora la aplicacion puede crear un usuario ADMIN y un usuario ALUMNO, el cual tendra acceso controlado por el admin
* v0.2.0 - Se cambiaron las estructuras de todos los formularios para hacerlos mas dinamicos con las ventanas del navegador (Se añadio NodeJs como conexion con el DOM y la BD)
* v1.0.0 - La aplicacion ya es funcional en la mayoria de sus modulos y puede ejecutarse en modo produccion



## Versionado 📌

Usamos [Git](https://git-scm.com/) para el versionado local de la app y [GitHub](https://github.com) para el trabajo con versionado remoto y colaborativo.

## [Despliegue en contenedores Docker](res/despliegue_Docker.md) 🟦

<img src="res/icons/docker.png" width="70">



## [Despliegue en contenedores Azure ](res/despliegue_Azure.md) 🔷

<img src="res/icons/azure.png" width="70">



**LA MAYORIA DE LOS PASOS SE HARAN DESDE AZURE CLI POR LO QUE HAY QUE TENERLO INSTALADO**


## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Jose Uriel Rodriguez Ramirez** - *Creacion del proyecto, Modulo de Alumnos, Grados e Interfaz* - [Jose-beat](https://github.com/Jose-beat)
* **Fatima Isabel Santiago Reynoso** - *Interfaz y modulo de Pagos* - [Fatima9007](https://github.com/Fatima9007)
* **Melissa Dominguez Guarneros** - *Documentación* - [Melissa8717-do](https://github.com/Melissa8717-do)
* **Miguel Sanchez Contreras** - *Sistema de Acceso* - [ayoy147](https://github.com/ayoy147)


---
Creditos y Saludos a _Andrés Villanueva_ - [Villanuevand](https://github.com/Villanuevand) y
Repositorio de la biblioteca de Iconos Azure a _RichardSlater_ - [Iconos](https://github.com/amido/azure-vector-icons/)