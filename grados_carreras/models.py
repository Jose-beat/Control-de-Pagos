from django.db import models

class Grados_carreras(models.Model):
    
    idCarrera = models.IntegerField(primary_key=True, default=6564)
    carrera = models.CharField(max_length=200, blank=True, null=True )
    grado = models.CharField(max_length=100, blank=True, null=True,  )

    class Meta:
        ordering=['idCarrera']

    def __str__(self):
        return str(self.idCarrera)
        