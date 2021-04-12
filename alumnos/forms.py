from django import forms

class RegistroAlumnos(forms.Form):
    matricula = forms.IntegerField()
    nombre =  forms.CharField()
    apellidos = forms.CharField()
    domicilio = forms.CharField()
    telefono = forms.CharField()
  #  grado =  forms.ModelMultipleChoiceField()
    email = forms.EmailField( required=False)
    beca = forms.IntegerField()