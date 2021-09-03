from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required
from .models import Pago
from .forms import FormRegistroPago, FormPago
from alumnos.models import Alumno
from cobros.models import Cobro
from django.contrib import messages
from .updates import act_tramite
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
        return render(request, 'index.html')
model = Pago


def registroPago(request):
        act_tramite()
        if request.method == 'POST':
            form = FormPago(request.POST)
            if form.is_valid():                  
                  form_data = form.cleaned_data
                  
                  try:
                        pagoM = Pago()
                        '''
                        '''
                       
                        pagoM.datos_cobro = Cobro.objects.get(nombre= str(form_data.get('datos_cobro')))
                        pagoM.datos_alumno = Alumno.objects.get(matricula= str(form_data.get('datos_alumno')))

                        pago = model.objects.create(

                                numero_tramite = form_data.get('numero_tramite'),

                                cantidad = form_data.get('cantidad'),

                                descuento = form_data.get('descuento'),

                                importe_total = form_data.get('importe_total'),

                                datos_cobro =  pagoM.datos_cobro,

                                datos_alumno = pagoM.datos_alumno,
                        )
                        
                        
                        messages.success(request, 'El pago se realizo exitosamente.')
                        return redirect(reverse('registroPagos'))
                  except Exception as e:
                        print("Desde la vista")
                        print(e)
                        pagos_totales = Pago.objects.all()
                        llave = form_data.get('numero_tramite')
                        
                        pagos_totales = Pago.objects.filter(
                              Q(numero_tramite__icontains = llave) 
                               )
                        if pagos_totales:
                              messages.error(request, 'El numero de tramite es invalido')
                        else:      
                              print(e)
                              messages.error(request, 'El pago no se efectuo correctamente')

                        return redirect(reverse('registroPagos'))
                  #new_alumno = form.save()
        else:
            print("NO HAY VALIDEZ")
            form = FormPago()

      



        
        return render(request, "pagos/registro_pagos.html",{'forms': form})



          
@login_required
def muestraPagos(request):

      queryset = request.GET.get("buscar")
      print(queryset)
      pagos_totales = Pago.objects.all()
      #Funcion de barra de busqueda 
      if queryset:
            pagos_totales = Pago.objects.filter(
                  Q(numero_tramite__icontains = queryset) 
                
            )
      #Seccion de paginacion 
      paginator = Paginator(pagos_totales, 7)
      page = request.GET.get('page')
      try:
            pagos = paginator.page(page)
      except PageNotAnInteger: 
            pagos = paginator.page(1)
      except EmptyPage:
            pagos = paginator.page(paginator.num_pages)



      return render(request, "pagos/muestra_pagos.html", {'pagos' : pagos})


@login_required
def pago(request, tramite_id):
      pass
      pago = get_object_or_404(Pago, numero_tramite=tramite_id)
      print(tramite_id)
      return render(request, 'pagos/pago.html', {'pago': pago})