from django.contrib import admin
from .models import Grados_carreras

class Grados_carreraAdmin(admin.ModelAdmin):
    list_display=('idCarrera', 'carrera', 'grado')
# Register your models here.
admin.site.register(Grados_carreras, Grados_carreraAdmin)