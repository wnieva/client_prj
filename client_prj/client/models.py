from django.db import models


class Client(models.Model):
    nombre = models.CharField(max_length=15, null=False, blank=False)
    ape_paterno = models.CharField(max_length=15, null=False, blank=False)
    ape_materno = models.CharField(max_length=15, null=True, blank=True)
    rut = models.CharField(max_length=10, unique=True,
                           null=False, blank=False)
    mail = models.CharField(max_length=60, unique=True, blank=True, null=True)
    num_movil = models.IntegerField(null=False, blank=False, unique=True)
    activo = models.BooleanField(True)
