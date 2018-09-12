from django.contrib import admin
from .models import Contacto
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombres',)
    
admin.site.register(Contacto, ContactoAdmin)