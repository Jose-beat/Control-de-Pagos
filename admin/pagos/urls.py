from django.urls import path
from django.contrib import admin

from .views import index, registroPago, muestraPagos, pago, pago_PDF, render_PDF, pdfListView

app_name: 'pago'
urlpatterns = [
    #path('', index, name="index"),
    path('', index, name="index"),
    path('RegistroPagos/', registroPago, name="registroPagos"),
    path('muestraPagos/', muestraPagos, name="muestraPagos"),
    path('pago/<int:tramite_id>', pago, name="pago"),
    path('pago_PDF/', pago_PDF, name="pago_PDF"),
    path('pago_PDF/', pdfListView.as_view(), name="pdfListView"),
    path('pdf/<int:tramite_id>', render_PDF, name="pdf"),
    
   
]