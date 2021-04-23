from django import forms
from .updates import act_matricula
from grados_carreras.models import Grados_carreras


carreras = []

try:
    carrera = Grados_carreras.objects.all()
    for i in carrera:
     carreras.append((i.idCarrera, i.carrera))
except:
    carreras = []


class RegistroAlumnos(forms.Form):
  
    matricula = forms.IntegerField( widget= forms.NumberInput(attrs={'readonly': True}))
    nombre =  forms.CharField()
    apellidos = forms.CharField()
    domicilio = forms.CharField()
    telefono = forms.CharField()
    grado =  forms.IntegerField()
    #grado = forms.MultipleChoiceField(choices=GRADOS)
    email = forms.EmailField( )
    beca = forms.IntegerField() 
    carrera = forms.ChoiceField(choices=carreras, required=True, label="Seleccione la carrera")
    matricula.widget.attrs.update({
        'value': act_matricula
        
        })
    