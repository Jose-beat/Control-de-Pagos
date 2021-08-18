from django.urls import path
from .views import registro_cobro, lista_cobros, editar_cobro, index, eliminar_cobro

urlpatterns = [
    path('', index, name="index"),
    path('registro_cobro/', registro_cobro, name="registro_cobro"),
    path('GuardarCobro/', registro_cobro, name="Guardarcobro"),
    path('lista_cobro/', lista_cobros, name="lista_cobros"),
    path('editar_cobro/<id>/', editar_cobro, name="editar_cobro"),
    path('eliminar_cobro/<id>/', eliminar_cobro, name="eliminar_cobro"),
]