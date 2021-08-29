from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Pago
from .forms import FormRegistroPago
from alumnos.models import Alumno
from cobros.models import Cobro
from django.contrib import messages
from .updates import act_tramite
from django.db.models import Q

def index(request):
        return render(request, 'index.html')
model = Pago


def registroPago(request):
        act_tramite()
        if request.method == 'POST':
            form = FormRegistroPago(request.POST)
            if form.is_valid():                  
                  form_data = form.cleaned_data
                  
                  try:
                        pagoM = Pago()
                        '''
                        '''
                        pagoM.datos_cobro = Cobro.objects.get(nombre= form_data.get('datos_cobro'))
                        pagoM.datos_alumno = Alumno.objects.get(matricula= form_data.get('datos_alumno'))

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

                        pagos_totales = Pago.objects.all()
                        llave = form_data.get('tramite')
                        
                        pagos_totales = Alumno.objects.filter(
                              Q(tramite__icontains = llave) 
                               )
                        if pagos_totales:
                              messages.error(request, 'El numero de tramite es invalido')
                        else:      
                              print(e)
                              messages.error(request, 'El pago no se efectuo correctamente')

                        return redirect(reverse('registroPago'))
                  #new_alumno = form.save()
        else:
            print("NO HAY VALIDEZ")
            form = FormRegistroPago()

      



        
        return render(request, "pagos/registro_pagos.html",{'forms': form})