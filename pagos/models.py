from django.db import models
from django.utils.timezone import now


class Pay(models.Model):
    name = models.CharField(max_length=100, 
        verbose_name="Nombre del pago")
    content = models.TextField(
        verbose_name="Descripcion")
    amount = models.IntegerField(
        verbose_name="Monto a Pagar", default=0)
    grant = models.BooleanField ( 
        verbose_name="Beca")
    created = models.DateTimeField( 
        verbose_name="Fecha de registro de pago")
    classification = models.CharField(max_length=100,
        verbose_name="Clasificacion")
  

    class Meta:
        verbose_name = "pago"
        verbose_name_plural = "pagos"

    def __str__(self):
        return self.name