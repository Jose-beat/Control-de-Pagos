from django.contrib import admin
from .models import Cobro
# Register your models here.
class CobroAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Cobro, CobroAdmin)