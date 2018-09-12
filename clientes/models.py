from django.db import models

# Create your models here.

def custom_upload_to(instance, filename):
    return 'clientes/logo/{0}/{1}'.format(instance.nombre, filename)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción")
    logo = models.ImageField(upload_to=custom_upload_to, null=True, blank=True, verbose_name="Logo")
    link = models.URLField(max_length=100, null=True, blank=True, verbose_name="Sitio Web")
    ck = models.PositiveIntegerField(verbose_name="Ck", null=True, blank=True)
    inicio = models.DateField(verbose_name="Inicio de Proyecto MOC", null=True, blank=True)
    fin = models.DateField(verbose_name="Fin de Proyecto MOC", null=True, blank=True)
    noc = models.BooleanField(verbose_name="NOC",  default=False)
    soc = models.BooleanField(verbose_name="SOC",  default=False)
    poc = models.BooleanField(verbose_name="POC",  default=False)
    boc = models.BooleanField(verbose_name="BOC",  default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre