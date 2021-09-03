from django.db import models
from admin.grados_carreras.models import Grados_carreras
#from django.forms import ModelForm

class Alumno(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_primero = models.CharField(max_length=100)
    apellido_segundo = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    grado = models.IntegerField()
    grupo = models.CharField(max_length=2, default="a")
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=10)
    beca = models.IntegerField()
    imagen_perfil = models.ImageField(upload_to='alumnos/')
    estado = models.BooleanField(default=True)
    justificacion_estado = models.CharField(max_length=100, default="")
    carrera = models.ForeignKey(Grados_carreras, on_delete=models.CASCADE)
    
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creacion"
    )
    
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de Edicion'
    )


    class Meta:
        ordering=['matricula']

    def __str__(self):
        return str(self.matricula)
