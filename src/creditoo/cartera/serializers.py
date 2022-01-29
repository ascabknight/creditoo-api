from rest_framework import serializers

from .models import AcuerdoPago, EstudioCredito, ObligacionFinanciera, Persona, CuentasPorCobrar

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre','tipo_identification', 'numero_identificacion')

class AcuerdoPagoSerializer(serializers.ModelSerializer):
    obligacion = serializers.SlugRelatedField(
        many=False, queryset=ObligacionFinanciera.objects.all(), slug_field='numero_referencia')

    class Meta:
        model = AcuerdoPago
        fields = ('__all__')

class ObligacionFinancieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObligacionFinanciera
        fields = ('__all__')



class EstudioCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudioCredito
        fields = ('__all__')


class CuentasPorCobrarSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(
        source='obligacion.cliente',
        read_only = True
    )

    nombre_deudor = serializers.CharField(
        source='obligacion.persona',
        read_only = True
    )

    numero_identificacion = serializers.CharField(
        source='obligacion.persona.numero_identificacion',
        read_only = True
    )

    class Meta:
        model = CuentasPorCobrar
        fields = ('__all__')