from django import forms
from .updates import act_matricula
from grados_carreras.models import Grados_carreras
from .models import Alumno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

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
carreras = []
#Añadir selectores en algunos formularios
justificaciones = [

]

try:
    carrera = Grados_carreras.objects.all()
    numero_grupos = 0
    for i in carrera:
     carreras.append((i.idCarrera, i.carrera))
     numero_grupos = i.cantidad_grupos
     print(carreras)
    
    
except:
    carreras = []


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
    carrera = forms.ChoiceField(choices=carreras, required=True, label="Seleccione la carrera")
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
            #"fecha": forms.NumberInput(attrs={'type': 'date'})
        }
    