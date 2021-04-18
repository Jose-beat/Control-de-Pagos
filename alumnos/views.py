from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from django.urls import reverse
#from .models import AlumnoForm
from  .forms import RegistroAlumnos as AlumnoForm
import datetime

model = Alumno
def registroAlumnos(request):
      #form = RegistroAlumnos()
      if request.method == 'POST':
            form = AlumnoForm(request.POST)
            if form.is_valid():                  
                  
                  form_data = form.cleaned_data
                  
                  alumno = model.objects.create(
                         matricula =form_data.get('matricula'),
                         nombre =   form_data.get('nombre'),
                         apellidos =form_data.get('apellidos'),
                         domicilio =form_data.get('domicilio'),
                         telefono = form_data.get('telefono'),
                         grado =    form_data.get('grado'),
                       email =       form_data.get('email'),
                         beca =     form_data.get('beca'),
                  )

                  return redirect(reverse('muestraAlumnos'))
                  
                  #new_alumno = form.save()
      else:
            form = AlumnoForm()

      #form = AlumnoForm()
      return render(request, "alumnos/registro_alumnos.html", {'forms': form})

def muestraAlumnos(request):

      alumnos = Alumno.objects.all()
      return render(request, "alumnos/muestra_alumnos.html", {'alumnos' : alumnos})

def alumno(request, alumno_id):
      pass
      alumno = get_object_or_404(Alumno, matricula=alumno_id)
      print(alumno_id)
      return render(request, 'alumnos/alumno.html', {'alumno': alumno})
