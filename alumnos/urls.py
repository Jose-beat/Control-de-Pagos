from django.contrib import admin
from django.urls import path
from alumnos import views

urlpatterns = [
    path('', views.muestraAlumnos, name='muestraAlumnos'),
    path('registroAlumnos/', views.registroAlumnos ,name='registroAlumnos'),
    path('<int:alumno_id>/', views.alumno, name='alumno' ),
    path('edit/<int:alumno_id>/', views.editarAlumno, name='editarAlumno' )
    
    

]
