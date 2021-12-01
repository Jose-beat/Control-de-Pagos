from django.db import models
from django.utils.timezone import now
from admin.alumnos.models import Alumno
#seleccion de menu

CLASIFICACION_CHOISE = [
    ('En Ventanilla', 'En Ventanilla'),
    ('En Linea', 'En Linea'),
   
  ]



class Cobro(models.Model):
    
    nombre = models.CharField(max_length=100, 
        verbose_name="Nombre del pago")
    descripcion = models.CharField(max_length=700,
        verbose_name="Descripcion")
    monto = models.IntegerField(
        verbose_name="Monto a Pagar", default=0)
    
    tipo_Cobro= models.TextField(choices=CLASIFICACION_CHOISE,
        verbose_name="Tipo de pago")

    aplica_descuento = models.BooleanField()
    
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creacion"
    )
    
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de Edicion'
    )

    class Meta:
        verbose_name = "cobro"
        verbose_name_plural = "cobros"

    def __str__(self):
        return self.nombre