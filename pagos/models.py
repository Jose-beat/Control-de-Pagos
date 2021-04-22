from django.db import models
from django.utils.timezone import now

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

#seleccion de mENO RADIO
RADIO_CHOISE = [
    ('si', 'Si'),
    ('no', 'No'),
    
  ]


class Pago(models.Model):
    
    nombre = models.CharField(max_length=100, 
        verbose_name="Nombre del pago")
    descripcion = models.CharField(max_length=700,
        verbose_name="Descripcion")
    monto = models.IntegerField(
        verbose_name="Monto a Pagar", default=0)
    beca= models.TextField(choices=RADIO_CHOISE,
        verbose_name="Beca")
    fecha = models.DateTimeField( 
        verbose_name="Fecha de registro de pago")
    tipo_pago= models.TextField(choices=CLASIFICACION_CHOISE,
        verbose_name="Tipo de pago")
  

    class Meta:
        verbose_name = "pago"
        verbose_name_plural = "pagos"

    def __str__(self):
        return self.nombre