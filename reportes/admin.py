from django.contrib import admin
from .models import Reportes
# Register your models here.

class ReportesAdmin(admin.ModelAdmin):
    pass
#list_display=('idCarrera', 'carrera', 'grado')

admin.site.register(Reportes, ReportesAdmin)