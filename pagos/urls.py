from django.urls import path
from .views import registro_pago, lista_pago, editar_pago, index, eliminar_pago, reporte

urlpatterns = [
    path('', index, name="index"),
    path('registro_pago/', registro_pago, name="registro_pago"),
    path('GuardarPago/', registro_pago, name="GuardarPago"),
    path('lista_pago/', lista_pago, name="lista_pago"),
    path('editar_pago/<id>/', editar_pago, name="editar_pago"),
    path('eliminar_pago/<id>/', eliminar_pago, name="eliminar_pago"),
    path('reporte/', reporte, name="reporte"),
]