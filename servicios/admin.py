from django.contrib import admin
from .models import Servicio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('cliente',)
    
admin.site.register(Servicio, ServicioAdmin)
