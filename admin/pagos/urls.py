from django.urls import path
from .views import index, registroPago, muestraPagos, pago
urlpatterns = [
    #path('', index, name="index"),
    path('', index, name="index"),
    path('RegistroPagos/', registroPago, name="registroPagos"),
    path('muestraPagos/', muestraPagos, name="muestraPagos"),
    path('pago/<int:tramite_id>', pago, name="pago")
   
]