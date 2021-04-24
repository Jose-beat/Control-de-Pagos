from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pagos.models import Pago
from alumnos.models import Alumno
from pagos.models import Pago
from .models import Reportes
from .forms import RegistroReportes, EditReporteForm
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .updates import act_idReporte
# Create your views here.
#@login_required
#<======================================REPORTES==============================================>

def registroReporte(request):
      #act_idReporte()
      model = Reportes    
      if request.method == 'POST':
            form = RegistroReportes(request.POST)
            if form.is_valid():                  
                  
                  form_data = form.cleaned_data
                  try:
                        reporte = Reportes()                  
                        reporte.alumno = Alumno.objects.get(matricula=form_data.get('matricula'))
                        reporte.cobro = Pago.objects.get(nombre=form.data.get('cobro'))
                        
                        reporte = model.objects.create(
                            
                            idReporte = form_data.get('idReporte'),
                            matricula = reporte.alumno,
                            cobro     = reporte.cobro,
                            nombreDeudor = form_data.get('nombreDeudor'),
                            grado = form_data.get('grado'),
                            carrera = form_data.get('carrera'),
                            cantidadDeudo = form_data.get('cantidadDeudo'),
                        )
              
                        messages.success(request, 'El alumno ha sido creado exitosamente.')
                        return redirect(reverse('registro'))

                  except Exception as e:

                        reportes_totales = Reportes.objects.all()
                        llave = form_data.get('idReporte')
                        
                        reportes_totales = Reportes.objects.filter(
                              Q(idReporte__icontains = llave) 
                               )
                        if reportes_totales:
                              messages.error(request, 'Dato Encontrado')
                              return redirect(reverse('registro'))
                        else:      
                              print(e)
                              messages.error(request, 'El alumno no se registro en el sistema.')

                        return redirect(reverse('registro'))
                  #new_alumno = form.save()
      else:
            form = RegistroReportes()
      
      
      return render(request, "reportes/registro.html", {'forms': form})



        
def reporte(request):
    
      queryset = request.GET.get("buscar")
      print(queryset)
      reportes_totales = Reportes.objects.all()
      #Funcion de barra de busqueda 
      if queryset:
            reportes_totales = Reportes.objects.filter(
                  Q(idReporte__icontains = queryset) 
                
            )
      #Seccion de paginacion 
      paginator = Paginator(reportes_totales, 7)
      page = request.GET.get('page')
      try:
            reportes = paginator.page(page)
      except PageNotAnInteger: 
            reportes = paginator.page(1)
      except EmptyPage:
            reportes = paginator.page(paginator.num_pages)
  
      return render(request,'reportes/vista.html', {'reportes' : reportes})

def verReporte(request, reporte_id):
      reporte = get_object_or_404(Reportes, idReporte=reporte_id)
      return render(request, 'reportes/reporte.html', {'reporte':reporte})

def EditarReporte(request, reporte_id):
      reporte = get_object_or_404(Reportes, idReporte=reporte_id)
      data = {
        'forms': EditReporteForm(instance=reporte)
       }
      if request.method =='POST':
            formulario = EditReporteForm(data=request.POST, instance=reporte)
            if formulario.is_valid():
                  formulario.save()
                  return redirect(to="vista")
            data["form"] = formulario
      
   
      return render(request, 'reportes/editarReporte.html',data)
