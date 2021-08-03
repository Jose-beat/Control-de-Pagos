from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Cobro
from .forms import CobroForm
from django.urls import reverse
from registration.models import Profile
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@permission_required('alumno.can_edit')
@login_required

def registro_cobro(request):
    data={
        'form': CobroForm()
    }
    if request.method =='POST':
        formulario = CobroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
        return redirect(reverse('lista_cobros'))


    return render(request, 'cobros/registro_cobro.html', data)

@login_required
def lista_cobros(request):
    cobros = Cobro.objects.all()
    data = {
        'cobros': cobros
    }
    return render(request,'cobros/lista_cobros.html', data)

@login_required
def editar_cobro(request, id):
    cobro =  get_object_or_404(Cobro, id=id)

    data = {
        'form': CobroForm(instance=cobro)
    }
    if request.method =='POST':
        formulario = CobroForm(data=request.POST, instance=cobro)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_cobro")
        data["form"] = formulario
   
    return render(request, 'cobros/editar_cobro.html', data)

@login_required
def eliminar_cobro(request, id):
    cobro =  get_object_or_404(Cobro, id=id)
    cobro.delete()
    return redirect(to="lista_cobro")
