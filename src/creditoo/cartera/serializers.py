from asyncore import read
from django.forms import SlugField
from rest_framework import serializers

from .models import AcuerdoPago, ObligacionFinanciera, Persona, CuentasPorCobrar


class PersonaSerializer(serializers.ModelSerializer):
    numero_identificacion = serializers.IntegerField(read_only=False)

    class Meta:
        model = Persona
        fields = ('__all__')


class AcuerdoPagoSerializer(serializers.ModelSerializer):
    obligacion = serializers.SlugRelatedField(
        many=False, read_only=False, queryset=ObligacionFinanciera.objects.all(), slug_field='numero_referencia')

    class Meta:
        model = AcuerdoPago
        fields = ('__all__')


class ObligacionFinancieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObligacionFinanciera
        fields = ('__all__')


class CuentasPorCobrarSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(
        source='obligacion.cliente',
        read_only=True
    )

    nombre_deudor = serializers.CharField(
        source='obligacion.persona',
        read_only=True
    )

    numero_identificacion = serializers.CharField(
        source='obligacion.persona.numero_identificacion',
        read_only=True
    )

    class Meta:
        model = CuentasPorCobrar
        fields = ('__all__')
