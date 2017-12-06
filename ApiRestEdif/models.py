from django.db import models
from django.utils import timezone

# Create your models here.
class Residente(models.Model):

    DUEÑO = 'dueño'
    ARRENDATARIO = 'arrendatario'

    TIPO_RESIDENTE = (
        (DUEÑO, 'dueño'),
        (ARRENDATARIO, 'arrendatario'),
    )

    rut = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellidomaterno = models.CharField(max_length=50)
    apellidopaterno = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_RESIDENTE)
    created_date = models.DateTimeField(default=timezone.now)
    fechavigencia = models.DateTimeField(default=timezone.now)

class D(models.Model):
    residente = models.ForeignKey(Residente,on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, primary_key=True)
    piso = models.IntegerField()
