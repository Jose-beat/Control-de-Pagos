from django.db import models
#from django.forms import ModelForm

class Alumno(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    grado = models.IntegerField()
    email = models.EmailField(max_length=254)
    beca = models.IntegerField()

    class Meta:
        ordering=['matricula']

    def __str__(self):
        return str(self.matricula)
