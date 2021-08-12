from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistroAlumnos as AlumnoForm, EditAlumnoForm
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from .models import Alumno
from .updates import act_matricula
import datetime
from grados_carreras.models import Grados_carreras
from registration.models import Profile
from django.contrib.auth.decorators import login_required

model = Alumno
@login_required
def registroAlumnos(request):

      
      act_matricula()
      if request.method == 'POST':
            form = AlumnoForm(request.POST ,request.FILES)
            if form.is_valid():                  
                  print("SI HAY VALIDEZ")
                  form_data = form.cleaned_data
                  try:
                        alumn = Alumno()
                        alumn.grado_carrera = Grados_carreras.objects.get(idCarrera= form_data.get('carrera'))
                        
                        alumno = model.objects.create(
                              matricula = form_data.get('matricula'),
                              nombre    = form_data.get('nombre'),
                              apellido_primero = form_data.get('apellido_primero'),
                              apellido_segundo = form_data.get('apellido_segundo'),
                              domicilio = form_data.get('domicilio'),
                              telefono  = form_data.get('telefono'),
                              grado     = form_data.get('grado'),
                              grupo     = form_data.get('grupo'),                                
                              carrera = alumn.grado_carrera,
                              email     = form_data.get('email'),
                              beca      = form_data.get('beca'),
                              imagen_perfil = form_data.get('imagen_perfil'),
                              estado = form_data.get('estado'),
                              justificacion_estado = form_data.get('justificacion_estado'),
                        )

                        
                        messages.success(request, 'El alumno ha sido creado exitosamente.')
                        return redirect(reverse('muestraAlumnos'))
                  except Exception as e:

                        alumnos_totales = Alumno.objects.all()
                        llave = form_data.get('matricula')
                        
                        alumnos_totales = Alumno.objects.filter(
                              Q(matricula__icontains = llave) 
                               )
                        if alumnos_totales:
                              messages.error(request, 'El alumno ya existe')
                        else:      
                              print(e)
                              messages.error(request, 'El alumno no se registro en el sistema.')

                        return redirect(reverse('registroAlumnos'))
                  #new_alumno = form.save()
      else:
            print("NO HAY VALIDEZ")
            form = AlumnoForm()

      
      return render(request, "alumnos/registro_alumnos.html", {'forms': form})

      
@login_required
def muestraAlumnos(request):

      queryset = request.GET.get("buscar")
      print(queryset)
      alumnos_totales = Alumno.objects.all()
      #Funcion de barra de busqueda 
      if queryset:
            alumnos_totales = Alumno.objects.filter(
                  Q(matricula__icontains = queryset) 
                
            )
      #Seccion de paginacion 
      paginator = Paginator(alumnos_totales, 7)
      page = request.GET.get('page')
      try:
            alumnos = paginator.page(page)
      except PageNotAnInteger: 
            alumnos = paginator.page(1)
      except EmptyPage:
            alumnos = paginator.page(paginator.num_pages)



      return render(request, "alumnos/muestra_alumnos.html", {'alumnos' : alumnos})
@login_required
def alumno(request, alumno_id):
      pass
      alumno = get_object_or_404(Alumno, matricula=alumno_id)
      print(alumno_id)
      return render(request, 'alumnos/alumno.html', {'alumno': alumno})
@login_required
def editarAlumno(request, alumno_id):
      alumno =  get_object_or_404(Alumno, matricula=alumno_id)
      data = {
        'form': EditAlumnoForm(instance=alumno),
        'alumno': alumno
      }
      if request.method =='POST':
            
            formulario = EditAlumnoForm(request.POST,request.FILES, instance=alumno)
            print("si HAY VALIDEZ" + str(formulario.is_valid()))
            if formulario.is_valid():
                  print("si HAY MAS VALIDEZ")
                  formulario.save()
                  return redirect(to="muestraAlumnos")
            data["form"] = formulario
      
   
      return render(request, 'alumnos/editar_alumnos.html',data)

