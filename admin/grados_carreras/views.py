from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroGrados, EditGradoForm
from .models import Grados_carreras
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from registration.models import Profile
from django.contrib.auth.decorators import login_required

model = Grados_carreras

@login_required
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
            
      return render(request, 'admin/grados_carreras/lista_carreras.html', {'grados' : grados})

@login_required

def registroGrados(request):

      if request.method == 'POST':
            form = RegistroGrados(request.POST)
            if form.is_valid():
                  form_data = form.cleaned_data
                  try:

                        GC = model.objects.create(
                              idCarrera=form_data.get('idCarrera'),
                              carrera=form_data.get('carrera'),
                              nivel = form_data.get('nivel'),
                              periodo = form_data.get('periodo'),
                              cantidad_grados=form_data.get('cantidad_grados'),
                              cantidad_grupos=form_data.get('cantidad_grupos'),
                        )
                        messages.success(
                            request, 'La carrera ha sido creado exitosamente.')
                        return redirect(reverse('muestraGrados'))
                  except:
                        carreras_totales = Grados_carreras.objects.all()
                        llave = form_data.get('idCarrera')

                        carreras_totales = Grados_carreras.objects.filter(
                              Q(idCarrera__icontains = llave)
                        )

                        if carreras_totales:
                              messages.error(request, 'La carrera ya existe')
                              print('Ya existe carnal')
                        else:
                              messages.error(
                                  request, 'La carrera no se registro en el sistema.')

                        return redirect(reverse('registroGrados'))
                  # new_alumno = form.save()
      else:
            form = RegistroGrados()
      return render(request, 'admin/grados_carreras/registro_carrera.html', {'form':form})

      
@login_required  
def editarGrado(request, carrera_id):
        carrera =  get_object_or_404(Grados_carreras, idCarrera=carrera_id)
        data = {
        'form': EditGradoForm(instance=carrera)
        }

        if request.method =='POST':
            formulario = EditGradoForm(data=request.POST, instance=carrera)
            if formulario.is_valid():
                  formulario.save()
                  return redirect(to="muestraGrados")
            data["form"] = formulario
      
   
        return render(request, 'admin/grados_carreras/editar_carrera.html',data)

@login_required
def Grado(request, carrera_id):
      carrera = get_object_or_404(Grados_carreras, idCarrera=carrera_id)
      print(carrera_id)
      return render(request, 'admin/grados_carreras/carrera.html', {'carrera': carrera})
