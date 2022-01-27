from django.db import models


class Persona(models.Model):
    readonly_fields = ('creado', 'actualizado')
    list_display = ("numero_identificacion", "nombre")

    numero_identificacion = models.BigIntegerField()
    tipo_identification = models.CharField(max_length=2, default='CC')
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    codigo_ref = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"


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
    estado_obligacion = models.CharField(max_length=150)
    fecha_ultimo_pago = models.DateField()
    tramo = models.CharField(max_length=150)
    dias_mora = models.IntegerField()
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
    fecha_compromiso = models.DateField(blank=True)
    valor_cuota = models.FloatField(null=False)
    comentarios = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.obligacion}"


class Recaudo(models.Model):
    obligacion = models.ForeignKey(
        ObligacionFinanciera, on_delete=models.CASCADE, verbose_name='Obligacion')
    estado_obligacion = models.CharField(max_length=150)
    fecha_pago_recaudo = models.DateField(null=True)
    tramo = models.CharField(max_length=150)
    valor_recaudo = models.FloatField()
