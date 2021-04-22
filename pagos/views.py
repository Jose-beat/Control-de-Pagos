from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago 
from .forms import PagoForm

def index(request):
    return render(request, 'pagos/index.html')

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


    return render(request, 'pagos/registro_pago.html', data)

def lista_pago(request):
    pagos = Pago.objects.all()
    data = {
        'pagos': pagos
    }
    return render(request,'pagos/lista_pago.html', data)

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

def eliminar_pago(request, id):
    pago =  get_object_or_404(Pago, id=id)
    pago.delete()
    return redirect(to="lista_pago")