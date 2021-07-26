from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.

# Create your models here.

class Persona(models.Model):
    TIPO_IDENTIFICACION = (
        ('CC', 'Cedula'),
        ('CE', 'Cedula Extranjeria'),
        ('PP', 'Pasaporte'),
    )

    numero_identificacion = models.BigIntegerField()
    tipo_identification = models.CharField(max_length=2, choices=TIPO_IDENTIFICACION, default='CC')
    fecha_expedicion = models.DateField(null=True)
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    url_logo = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ObligacionFinanciera(models.Model):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Deudor')
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name='Cliente')
    numero_referencia = models.CharField(max_length=100)
    estado_obligacion = models.CharField(max_length=150)
    fecha_ultimo_pago = models.DateField(null=True)
    dias_mora = models.IntegerField()
    saldo_vencido = models.FloatField()

    class Meta:
        verbose_name = 'Obligacion Financiera'
        verbose_name_plural = 'Obligaciones Financieras'

    


