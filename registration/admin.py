from django.contrib import admin

class RegistrationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
# Register your models here.
