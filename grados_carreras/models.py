from django.db import models

class Grados_carreras(models.Model):
    
    idCarrera = models.CharField(max_length=5 , primary_key=True, default="---")
    carrera = models.CharField(max_length=200, blank=True, null=True )
    nivel = models.CharField(max_length=100, blank=True, null=True,  )
    cantidad_grados = models.IntegerField()
    cantidad_grupos = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creacion"
    )
    
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de Edicion'
    )

    class Meta:
        ordering=['carrera']

    def __str__(self):
        return str(self.carrera)
        