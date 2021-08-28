from django.urls import path
from .views import index, registroPago
urlpatterns = [
    #path('', index, name="index"),
    path('', index, name="index"),
    path('RegistroPagos', registroPago, name="registroPagos"),
   
]