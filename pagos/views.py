from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago 
from .forms import PagoForm
from django.urls import reverse
from registration.models import Profile
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'pagos/index.html')


@login_required
def registro_pago(request):
    data={
        'form': PagoForm()
    }
    if request.method =='POST':
        formulario = PagoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
        return redirect(reverse('lista_pago'))


    return render(request, 'pagos/registro_pago.html', data)

@login_required
def lista_pago(request):
    pagos = Pago.objects.all()
    data = {
        'pagos': pagos
    }
    return render(request,'pagos/lista_pago.html', data)

@login_required
def editar_pago(request, id):
    pago =  get_object_or_404(Pago, id=id)

    data = {
        'form': PagoForm(instance=pago)
    }
    if request.method =='POST':
        formulario = PagoForm(data=request.POST, instance=pago)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_pago")
        data["form"] = formulario
   
    return render(request, 'pagos/editar_pago.html', data)

@login_required
def eliminar_pago(request, id):
    pago =  get_object_or_404(Pago, id=id)
    pago.delete()
    return redirect(to="lista_pago")
