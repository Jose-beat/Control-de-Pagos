from django.urls import path
from .views import registro_cobro, lista_cobros, editar_cobro, eliminar_cobro, modalCobro

urlpatterns = [
    path('registro_cobro/', registro_cobro, name="registro_cobro"),
    path('GuardarCobro/', registro_cobro, name="Guardarcobro"),
    path('lista_cobro/', lista_cobros, name="lista_cobros"),
    path('editar_cobro/<id>/', editar_cobro, name="editar_cobro"),
    path('ver_cobros/', modalCobro, name="ver_cobro"),
    path('eliminar_cobro/<id>/', eliminar_cobro, name="eliminar_cobro"),
]