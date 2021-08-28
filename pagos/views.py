from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required

def index(request):
        return render(request, 'index.html')

def registroPago(request):
    return render(request, "pagos/registro_pagos.html")