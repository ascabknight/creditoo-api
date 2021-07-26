from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.

# Create your models here.

class Persona(models.Model):
    readonly_fields = ('creado', 'actualizado')
    TIPO_IDENTIFICACION = (
        ('CC', 'Cedula'),
        ('CE', 'Cedula Extranjeria'),
        ('PP', 'Pasaporte'),
    )

    numero_identificacion = models.BigIntegerField()
    tipo_identification = models.CharField(max_length=2, choices=TIPO_IDENTIFICACION, default='CC')
    fecha_expedicion = models.DateField(null=True, blank=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_completo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    url_logo = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ObligacionFinanciera(models.Model):
    readonly_fields = ('creado', 'actualizado')
    
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Deudor')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    numero_referencia = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Obligacion Financiera'
        verbose_name_plural = 'Obligaciones Financieras'

class ActualizacionObligacion(models.Model):
    readonly_fields = ('creado', 'actualizado')

    obligacion = models.ForeignKey(ObligacionFinanciera, verbose_name='Obligacion Financiera')
    periodo = models.CharField(max_length=100)
    estado_obligacion = models.CharField(max_length=150)
    fecha_ultimo_pago = models.DateField(null=True)
    tramo_inicial = models.CharField(max_length=150)
    dias_mora = models.IntegerField()
    saldo_vencido = models.FloatField(verbose_name="Saldo en Mora")
    total_pagar = models.FloatField(verbose_name="Total a Pagar")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Obligacion'
        verbose_name_plural = 'Tramos de Obligacion'

class AcuerdoPago(models.Model):
    readonly_fields = ('creado', 'actualizado')

    obligacion = models.ForeignKey(ObligacionFinanciera, verbose_name='Obligacion Financiera')
    cuotas = models.IntegerField()
    valor_cuota = models.FloatField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Recaudo(models.Model):
    obligacion = models.ForeignKey(ObligacionFinanciera, verbose_name='Obligacion Financiera')

