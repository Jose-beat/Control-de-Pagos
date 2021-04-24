from django.urls import path
from reportes import views

urlpatterns = [
  path('',views.reporte, name="vista"),
  path('reporte/',views.reporte, name="reporte"),
  path('registro/',views.registroReporte, name="registro"),
  path('<int:reporte_id>/', views.verReporte, name='verReporte' ),
  path('edit/<int:reporte_id>/', views.EditarReporte, name='editarReporte' )
]


