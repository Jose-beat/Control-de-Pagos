from django.db import models
# Create your models here.
from django.db import models
from django.utils.timezone import now
from alumnos.models import Alumno
#seleccion de menu

CLASIFICACION_CHOISE = [
    ('Inscripción', 'Inscripción'),
    ('Reinscripción', 'Reinscripción'),
    ('Intereses', 'Intereses'),
    ('Colegiatura', 'Colegiatura'),
    ('Conatancias', 'Conatancias'),
    ('Kardex', 'Kardex'),
    ('Credencial', 'Credencial'),
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