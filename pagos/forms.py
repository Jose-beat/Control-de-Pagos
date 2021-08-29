from django import forms
from .updates import act_tramite
from cobros.models import Cobro
from alumnos.models import Alumno

COBROS=[]
ALUMNOS=[]

try:
    
    cobro = Cobro.objects.all()
    alumno = Alumno.objects.all()
    #numero_grados = 0
    for i in cobro:
     COBROS.append((i.nombre, i.nombre))

    for j in alumno:
        ALUMNOS.append((j.matricula, j.nombre))
except Exception as e:
     print(e)
     
     
class FormRegistroPago(forms.Form):
    numero_tramite = forms.IntegerField()


    cantidad = forms.IntegerField()

    descuento = forms.IntegerField()

    importe_total = forms.IntegerField()

    datos_cobro =  forms.ChoiceField(choices=COBROS)

    datos_alumno = forms.ChoiceField(choices=ALUMNOS)

    numero_tramite.widget.attrs.update({
         'value': act_tramite
    })