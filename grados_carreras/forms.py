from django import forms

class RegistroGrados(forms.Form):
  
    idCarrera = forms.IntegerField( widget= forms.NumberInput())
    carrera =  forms.CharField()
    grado = forms.CharField()