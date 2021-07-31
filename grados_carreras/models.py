from django.db import models

class Grados_carreras(models.Model):
    
    idCarrera = models.CharField(max_length=5 , primary_key=True, default="---")
    carrera = models.CharField(max_length=200, blank=True, null=True )
    nivel = models.CharField(max_length=100, blank=True, null=True,  )
    grado = models.IntegerField()
    cantidad_grupos = models.IntegerField()
    class Meta:
        ordering=['idCarrera']

    def __str__(self):
        return str(self.idCarrera)
        