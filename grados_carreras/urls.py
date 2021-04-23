from django.contrib import admin
from django.urls import path
from grados_carreras import views

urlpatterns = [
    path('', views.muestraGrados, name='muestraGrados'),
    path('registroGrados/', views.registroGrados, name='registroGrados'),
    path('carrera/<int:carrera_id>', views.Grado, name='Grado')

]
