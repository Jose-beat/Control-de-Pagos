 # DEFINIMOS LA VERSION DE PYTHON
    FROM python:3.9.2
    
    # CREAMOS Y DEFINIMOS EL DIRECTORIO DE TRABAJO
    RUN mkdir /usr/src/app
    WORKDIR /usr/src/app

    # DEFINIMOS VARIABLES DE ENTORNO
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    # INSTALAMOS DEPENDENCIAS
    RUN pip install --upgrade pip 

    COPY ./requirements.txt /usr/src/app/

    RUN pip install -r requirements.txt

    # COPIAMOS EL PROYECTO 
    COPY . /usr/src/app/
    # EJECUTAMOS LAS MIGRACIONES
    RUN python manage.py makemigrations

    RUN python manage.py migrate --run-syncdb
    # SEMBRAMOS LOS DATOS DE EJEMPLO
    RUN python manage.py loaddata grados_seeders

    RUN python manage.py loaddata alumnos_seeders
    #ABRIMOS EL PUERTO 8000
    EXPOSE 8000

    #DEFINIMOR EL COMANDO DE ARRANQUE DEL SERVIDOR
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]