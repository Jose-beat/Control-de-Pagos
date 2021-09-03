from django import forms
from .updates import act_matricula, act_Grados_Carreras
from admin.grados_carreras.models import Grados_carreras
from .models import Alumno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from django.forms.widgets import Select, SelectMultiple, PasswordInput, NumberInput, Input
GRUPOS = [
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
GRADOS = []
BECAS = [
    ("0", "Sin Beca"),
    ("100","Beca de Excelencia (100%)" ),
    ("50", "Beca de Excelencia (50%)"),
    
]
JUSTIFICACIONES = [
    ('No Necesaria','No Necesaria'),
    ('Baja Temporal','Baja Temporal'),
    ('Baja Definitiva', 'Baja Definitiva'),
    ('Graduado', 'Graduado'),

]

try:
    
    carrera = Grados_carreras.objects.all()
    numero_grupos = 0
    #numero_grados = 0
    for i in carrera:
     CARRERAS.append((i.idCarrera, i.carrera))
     numero_grupos = i.cantidad_grupos
     #numero_grados = i.cantidad_grados
     
    
    for j in range(0,12):
        
        GRADOS.append((j, j))
    
except:
    CARRERAS = []

#Este formulario ha sido descartado y proximamente ELIMINADO
class RegistroAlumnos(forms.Form):
    matricula = forms.IntegerField( widget= forms.NumberInput(attrs={'readonly': True}))
    nombre =  forms.CharField()
    apellido_primero = forms.CharField()
    apellido_segundo = forms.CharField()
    domicilio = forms.CharField()
    telefono = forms.CharField()
    grado =  forms.ChoiceField(choices=GRADOS, required=True, label="Grado")
    grupo = forms.ChoiceField(choices=GRUPOS[0:numero_grupos], required = True, label="Grupo")
    #grupo = forms.ChoiceField(choices=GRUPOS, required = True, label="Grupo")
    email = forms.EmailField( )
    password = forms.CharField(widget= forms.PasswordInput())
    #beca = forms.IntegerField() 
    beca = forms.ChoiceField(choices=BECAS, required=True, label="Becas")
    carrera = forms.ChoiceField(choices=CARRERAS, label="Seleccione la carrera" )
    imagen_perfil = forms.ImageField(label='Foto de Perfil')
    estado = forms.BooleanField()
    justificacion_estado = forms.ChoiceField(choices=JUSTIFICACIONES, label="Justificacion")
    
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
            #'grupo': Select(choices=grupo_lista[0:numero_grupos]),
            'matricula': NumberInput(attrs={'readonly':True}),
            'beca': Select(choices=BECAS),
            'grado': Select(choices=GRADOS),
            'grupo': Select(choices=GRUPOS),
            'justificacion_estado': Select(choices=JUSTIFICACIONES),
            'password' : Input(attrs={'type':'password'})
            
            #'carrera': Select(choices=CARRERAS)
        }
class AlumnoFormM(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            #'grupo': Select(choices=grupo_lista[0:numero_grupos]),
            'matricula': NumberInput(attrs={'readonly':True,  'value': act_matricula}),
            'beca': Select(choices=BECAS),
            'grado': Select(choices=GRADOS),
            'grupo': Select(choices=GRUPOS),
            'justificacion_estado': Select(choices=JUSTIFICACIONES),
            'password' : Input(attrs={'type':'password'})
            
            #'carrera': Select(choices=CARRERAS)
        }
