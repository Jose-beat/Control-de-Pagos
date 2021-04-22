from django import forms
from .updates import act_matricula


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

    matricula.widget.attrs.update({
        'value': act_matricula
        
        })
    