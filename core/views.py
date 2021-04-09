from django.shortcuts import render

def home(request):
    return render(request, "core/login.html")

def registro(request):
    return render(request, "core/registro.html")

def registro_alumno(request):
    return render(request, "core/registro_alumno.html")