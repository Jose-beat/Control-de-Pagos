from django import forms
from .updates import act_matricula
from grados_carreras.models import Grados_carreras
from .models import Alumno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


carreras = []

try:
    carrera = Grados_carreras.objects.all()
    for i in carrera:
     carreras.append((i.idCarrera, i.carrera))
     print(carreras)
except:
    carreras = []

class RegistroAlumnos(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'alumno-form'
        self.helper.layout = Layout(
            'nombre',
            
        )
  
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

class EditAlumnoForm(forms.ModelForm):


    class Meta:

        model=Alumno
        fields = '__all__'

        widgets = {
            #"fecha": forms.NumberInput(attrs={'type': 'date'})
        }
    