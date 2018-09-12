from django.db import models
from clientes.models import Cliente

# Create your models here.

class Contacto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cargo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cargo")
    nivel = models.SmallIntegerField(verbose_name="nivel", default=1)
    email = models.EmailField(max_length=100, verbose_name="Email")
    telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name="Teléfono")
    celular = models.CharField(max_length=15, verbose_name="Celular")
    horario = models.CharField(max_length=10, null=True, blank=True, verbose_name="Horario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['nivel']

    def __str__(self):
        return self.nombres