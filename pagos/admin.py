from django.contrib import admin
from pagos.models import Pago

class PagoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('numero_tramite',)

admin.site.register(Pago, PagoAdmin)


