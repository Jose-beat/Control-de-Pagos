from django.forms.widgets import SelectMultiple, Select
from django import forms
from .models import Grados_carreras

NIVEL = [
    ('Licenciatura', 'Licenciatura'),
    ('Ingenieria', 'Ingenieria'),
    ('Posgrado', 'Posgrado'),
    ('Maestria', 'Maestria'),
]
GRADOS = []
GRUPOS = []
for i in range(1,13):
    GRADOS.append((i,i))
    GRUPOS.append((i,i))

class RegistroGrados(forms.Form):
  
    idCarrera = forms.CharField(max_length=5)
    carrera =  forms.CharField()
    nivel = forms.ChoiceField(choices=NIVEL, label="Nivel de Estudio")
    cantidad_grados = forms.ChoiceField(choices=GRADOS, label="Cantidad de Grados")
    cantidad_grupos = forms.ChoiceField(choices=GRUPOS, label="Cantidad de Grupos")
    

class EditGradoForm(forms.ModelForm):


    class Meta:

        model=Grados_carreras
        fields = ['idCarrera', 'carrera', 'nivel', 'cantidad_grados', 'cantidad_grupos']
        
        widgets = {
            'nivel': Select(choices=NIVEL)
        }