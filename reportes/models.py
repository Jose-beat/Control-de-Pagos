from django.db import models
from alumnos.models import Alumno
from pagos.models import Pago

class Reportes(models.Model):
    
    idReporte = models.IntegerField(primary_key=True,  default=0000 )
    matricula = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cobro     = models.ForeignKey(Pago, on_delete=models.CASCADE)
    nombreDeudor = models.CharField(max_length=100, blank=True, null=True)
    grado = models.IntegerField(verbose_name="Grado", default=0)
    carrera = models.CharField(max_length=100, blank=True, null=True)
    cantidadDeudo = models.IntegerField(verbose_name="Monto a Pagar", default=0)
    nombrePago = models.IntegerField(verbose_name="Nombre del Pago", default=0)
    descripcionPago = models.IntegerField(verbose_name="Descripcion del Pago", default=0)
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        return str(self.idReporte)
