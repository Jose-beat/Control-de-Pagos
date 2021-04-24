from django import forms
from .models import Grados_carreras
class RegistroGrados(forms.Form):
  
    idCarrera = forms.IntegerField( widget= forms.NumberInput())
    carrera =  forms.CharField()
    grado = forms.CharField()


class EditGradoForm(forms.ModelForm):


    class Meta:

        model=Grados_carreras
        fields = '__all__'

        widgets = {
            #"fecha": forms.NumberInput(attrs={'type': 'date'})
        }
    