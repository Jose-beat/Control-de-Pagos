from django import forms
from .updates import act_matricula
from grados_carreras.models import Grados_carreras
from .models import Alumno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from django.forms.widgets import Select, SelectMultiple
grupo_lista = [
    ('A','a'),
    ('B','b'),
    ('C','c'),
    ('D','d'),
    ('E','e'),
    ('F','f'),
    ('G','g'),
    ('H','h'),
    ('I','i'),
    ('J','j'),
]
CARRERAS = []
#Añadir selectores en algunos formularios
justificaciones = [
    
]

try:
    carrera = Grados_carreras.objects.all()
    numero_grupos = 0
    for i in carrera:
     CARRERAS.append((i.carrera, i.carrera))
     
     numero_grupos = i.cantidad_grupos
     print(CARRERAS)
    
    
except:
    CARRERAS = []


class RegistroAlumnos(forms.Form):
    matricula = forms.IntegerField( widget= forms.NumberInput(attrs={'readonly': True}))
    nombre =  forms.CharField()
    apellidos = forms.CharField()
    domicilio = forms.CharField()
    telefono = forms.CharField()
    grado =  forms.IntegerField()
    grupo = forms.ChoiceField(choices=grupo_lista[0:numero_grupos], required = True, label="Grupo")
    #grado = forms.MultipleChoiceField(choices=GRADOS)
    email = forms.EmailField( )
    beca = forms.IntegerField() 
    carrera = forms.ChoiceField(choices=CARRERAS, label="Seleccione la carrera" )
    imagen_perfil = forms.ImageField(label='Foto de Perfil')
    estado = forms.BooleanField()
    justificacion_estado = forms.CharField()
    imagen_perfil.widget.attrs.update({
        'id' : "imagenPerfil",
      
    })
    matricula.widget.attrs.update({
        'value': act_matricula
        
        })

class EditAlumnoForm(forms.ModelForm):
  


    class Meta:
 
        model=Alumno
        fields = '__all__'
        widgets = {
            'grupo': Select(choices=grupo_lista[0:numero_grupos]),
            #'carrera': Select(choices=CARRERAS)
        }
    