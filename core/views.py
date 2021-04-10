from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "core/login.html")

def registro(request):
    return render(request, "core/registro.html")

def registro_alumno(request):
    return render(request, "core/registro_alumno.html")

def registro_pago(request):
    return render(request, "core/registro_pago.html")