from django.shortcuts import render, HttpResponse



def user(request):
    return render(request, "usuari_alumno/perfil.html")
