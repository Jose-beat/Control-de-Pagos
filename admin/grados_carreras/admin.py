from django.contrib import admin
from .models import Grados_carreras

class Grados_carreraAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created', 'updated')
    list_display=('idCarrera', 'carrera', 'cantidad_grados')
# Register your models here.
admin.site.register(Grados_carreras, Grados_carreraAdmin)