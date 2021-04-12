from django.shortcuts import render, get_object_or_404
from .models import Alumno
from .models import AlumnoForm
import datetime

model = Alumno
def registroAlumnos(request):
      #form = RegistroAlumnos()
      if request.method == 'POST':
            form = AlumnoForm(request.POST)
            if form.is_valid():                  
                  new_alumno = form.save()
      else:
            form = AlumnoForm()

      return render(request, "registro_alumnos.html", {'forms': form})

def muestraAlumnos(request):

      alumnos = Alumno.objects.all()
      return render(request, "muestra_alumnos.html", {'alumnos' : alumnos})

def alumno(request, alumno_id):
      pass
      alumno = get_object_or_404(Alumno, matricula=alumno_id)
      print(alumno_id)
      return render(request, 'alumno.html', {'alumno': alumno})
