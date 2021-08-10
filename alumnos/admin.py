from django.contrib import admin
from .models import Alumno
# Register your models here.

#admin.site.register(Alumno)

class AlumnoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('matricula', 'nombre', 'apellidos')

admin.site.register(Alumno, AlumnoAdmin)
