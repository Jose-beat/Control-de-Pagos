from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroGrados
from .models import Grados_carreras
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages

model = Grados_carreras


def muestraGrados(request):
    
      queryset = request.GET.get("buscar")
      print(queryset)
      grados_totales = Grados_carreras.objects.all()
      #Funcion de barra de busqueda 
      if queryset:
            grados_totales = Grados_carreras.objects.filter(
                  Q(idCarrera__icontains = queryset) 
                
            )
      #Seccion de paginacion 
      paginator = Paginator(grados_totales, 7)
      page = request.GET.get('page')
      try:
            grados = paginator.page(page)
      except PageNotAnInteger: 
            grados = paginator.page(1)
      except EmptyPage:
            grados = paginator.page(paginator.num_pages)
            
      return render(request, 'grados_carreras/index.html', {'grados' : grados})


def registroGrados(request):

      if request.method == 'POST':
            form = RegistroGrados(request.POST)
            if form.is_valid():
                  form_data = form.cleaned_data
                  try:

                        GC = model.objects.create(
                              idCarrera=form_data.get('idCarrera'),
                              carrera=form_data.get('carrera'),
                              grado=form_data.get('grado'),
                        )
                        messages.success(
                            request, 'La carrera ha sido creado exitosamente.')
                        return redirect(reverse('muestraGrados'))
                  except:
                        carreras_totales = Grados_carreras.objects.all()
                        llave = form_data.get('idCarrera')

                        if carreras_totales:
                              messages.error(request, 'El alumno ya existe')
                        else:
                              messages.error(
                                  request, 'El alumno no se registro en el sistema.')

                        return redirect(reverse('registroGrados'))
                  # new_alumno = form.save()
      else:
            form = RegistroGrados()
      return render(request, 'grados_carreras/registros.html', {'form':form})

      
    

def Grado(request, carrera_id):
      carrera = get_object_or_404(Grados_carreras, idCarrera=carrera_id)
      print(carrera_id)
      return render(request, 'grados_carreras/carrera.html', {'carrera': carrera})
