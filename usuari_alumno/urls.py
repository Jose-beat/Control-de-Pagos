from django.contrib import admin
from django.urls import path
from usuari_alumno import views

urlpatterns = [
    path('', views.user, name='user'),
    
]
