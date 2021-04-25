from django import forms
from grados_carreras.models import Grados_carreras
from alumnos.models import Alumno
from pagos.models import Pago
from .models import Reportes
from .updates import act_idReporte

alumnos_locales = []
pagos_locales = []
nombre = ""
gradoAlumno = 0
carreraAlumno = ""
deuda = ""
try:
    alumnos = Alumno.objects.all()
    pagos = Pago.objects.all()

    for i in alumnos:
     alumnos_locales.append((i.matricula, i.matricula))
     nombre = i.nombre + " " + i.apellidos
     gradoAlumno = i.grado
     carreraAlumno = i.carrera.carrera
    print(alumnos)

    

    for j in pagos:
        pagos_locales.append((j.nombre,j.nombre))
        deuda = j.monto
    print(deuda)
    print(pagos)
    
except  Exception as e:

    alumnos = []
    pagos = []
    print(e)




class RegistroReportes(forms.Form):
    
    idReporte = forms.IntegerField( widget= forms.NumberInput(attrs={'readonly': True}))
    matricula = forms.ChoiceField(choices=alumnos_locales, required=True, label="Seleccione la carrera")
    cobro     = forms.ChoiceField(choices=pagos_locales, required=True, label="Seleccione la carrera")
    nombreDeudor = forms.CharField( max_length=100, required=False)
    grado = forms.IntegerField( required=False)
    carrera = forms.CharField( max_length=100, required=False)
    cantidadDeudo = forms.IntegerField( required=False)
    
    idReporte.widget.attrs.update({
            'value': act_idReporte()
    })

    nombreDeudor.widget.attrs.update({
        'value': nombre
    })

    grado.widget.attrs.update({
        'value':gradoAlumno
    })

    carrera.widget.attrs.update({
        'value':carreraAlumno
    })

    cantidadDeudo.widget.attrs.update({
        'value': deuda
    })

class EditReporteForm(forms.ModelForm):


    class Meta:

        model=Reportes
        fields = '__all__'

        widgets = {
            #"fecha": forms.NumberInput(attrs={'type': 'date'})
            
        }
    