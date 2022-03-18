from django.db import models
from django.db.models.base import Model


class Persona(models.Model):
    readonly_fields = ('creado', 'actualizado')
    list_display = ("numero_identificacion", "nombre_completo")

    numero_identificacion = models.IntegerField(unique=True)
    tipo_identification = models.CharField(max_length=2, default='CC')
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    nombre_departamento = models.CharField(
        max_length=100, verbose_name='Nombre Departamento')
    nombre_ciudad = models.CharField(
        max_length=100, verbose_name='Nombre Ciudad')
    nombre_barrio = models.CharField(
        max_length=100, verbose_name='Nombre Barrio')
    direccion = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_completo}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    url_logo = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ObligacionFinanciera(models.Model):
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Deudor')
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    numero_referencia = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_referencia

    class Meta:
        verbose_name = 'Obligacion Financiera'
        verbose_name_plural = 'Obligaciones Financieras'


class CuentasPorCobrar(models.Model):
    readonly_fields = ('creado', 'actualizado')

    obligacion = models.ForeignKey(
        ObligacionFinanciera, on_delete=models.CASCADE, verbose_name='Obligacion')
    periodo = models.CharField(max_length=100)
    estado_obligacion = models.CharField(max_length=150)
    fecha_ultimo_pago = models.DateTimeField(blank=True, null=True)
    fecha_limite_pago = models.DateTimeField()
    tramo = models.CharField(max_length=150)
    dias_mora = models.IntegerField(blank=True, null=True)
    saldo_vencido = models.FloatField(verbose_name="Saldo en Mora")
    total_pagar = models.FloatField(verbose_name="Total a Pagar")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cuenta por cobrar'
        verbose_name_plural = 'Cuentas por Cobrar'


class AcuerdoPago(models.Model):
    readonly_fields = ('creado', 'actualizado')

    obligacion = models.ForeignKey(
        ObligacionFinanciera, on_delete=models.CASCADE, verbose_name='Obligacion')
    cuotas = models.IntegerField()
    fecha_compromiso = models.DateField()
    valor_cuota = models.FloatField()
    estado = models.BooleanField(default=False)
    comentarios = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.obligacion

    class Meta:
        verbose_name = 'Acuerdo de pago'
        verbose_name_plural = 'Acuerdos de pago'
