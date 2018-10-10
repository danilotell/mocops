from django.db import models
from clientes.models import Cliente 

# Create your models here.

class Servicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nocdis = models.BooleanField(verbose_name="Monitoreo de disponibilidad",  default=False)
    noccap = models.BooleanField(verbose_name="Monitoreo de capacidad",  default=False)
    nocmet = models.BooleanField(verbose_name="Gestión de métricas de supervisión",  default=False)
    nocsim = models.BooleanField(verbose_name="Administración de información de seguridad",  default=False)
    nocinv = models.BooleanField(verbose_name="Gestión de inventarios",  default=False)
    nocdescripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción servicios NOC")

    socsiem = models.BooleanField(verbose_name="Gestión de eventos e información de seguridad",  default=False)
    socthreat = models.BooleanField(verbose_name="Gestión de Amenazas o Anomalías",  default=False)
    socrisk = models.BooleanField(verbose_name="Gestón de escenarios de riesgo",  default=False)
    soccomp = models.BooleanField(verbose_name="Gestión de cumplimiento",  default=False)
    socinc = models.BooleanField(verbose_name="Gestión de incidentes",  default=False)
    socfim = models.BooleanField(verbose_name="Monitoreo de integridad de archivos",  default=False)
    socdescripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción servicios SOC")

    poceh = models.BooleanField(verbose_name="Ethical Hacking",  default=False)
    pocgv = models.BooleanField(verbose_name="Gestión de vulnerabilidades",  default=False)
    pocav = models.BooleanField(verbose_name="Análisis de vulnerabilidades",  default=False)
    pocadm = models.BooleanField(verbose_name="Administracion delegada",  default=False)
    pocapt = models.BooleanField(verbose_name="Monitoreo de amenazas persistentes",  default=False)
    pochpot = models.BooleanField(verbose_name="Deception services",  default=False)
    poceducate = models.BooleanField(verbose_name="MOC Educate - Gestión del cambio",  default=False)
    pochsas = models.BooleanField(verbose_name="Software - Hardware As Services",  default=False)
    pocdescripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción servicios POC")

    bocga = models.BooleanField(verbose_name="Gestión de Activos",  default=False)
    bocge = models.BooleanField(verbose_name="Gestión de Eventos",  default=False)
    bocgi = models.BooleanField(verbose_name="Gestión de Incidentes",  default=False)
    bocri = models.BooleanField(verbose_name="Gestión de Riesgos",  default=False)
    boccump = models.BooleanField(verbose_name="Gestión de Cumplimiento",  default=False)
    bocplan = models.BooleanField(verbose_name="Gestión de Planes",  default=False)
    bocind = models.BooleanField(verbose_name="Gestión de Indicadores",  default=False)
    boccs = models.BooleanField(verbose_name="Gestión de Ciberseguridad",  default=False)
    bocdescripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción servicios BOC")


    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"