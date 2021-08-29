from django.db import models

'''

    Numero de Tramite (id)
    cantidad
    Descuento(Beca)
    Importe total 

    DATOS PARA LOS PAGOS
    Datos del alumno
    Datos del cobro 
    AÑADIR API CAPTCHA

'''

class Pago(models.Model):
    numero_tramite = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    descuento = models.CharField(max_length=100)
    importe_total = models.IntegerField()
    datos_cobro =  models.ForeignKey("cobros.Cobro", on_delete=models.CASCADE)
    datos_alumno = models.ForeignKey("alumnos.Alumno", on_delete=models.CASCADE)
    
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creacion"
    )
    
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de Edicion'
    )
    class Meta:
            ordering=['numero_tramite']

    def __str__(self):
        return str(self.numero_tramite)