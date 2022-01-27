from rest_framework import serializers

from .models import ObligacionFinanciera, Persona, CuentasPorCobrar, AcuerdoPago


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'tipo_identification',
                  'numero_identificacion')


class ObligacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObligacionFinanciera
        fields = ('__all__')


class AcuerdoPagoSerializer(serializers.ModelSerializer):
    obligacion = serializers.SlugRelatedField(
        many=False, queryset=ObligacionFinanciera.objects.all(), slug_field='numero_referencia')

    class Meta:
        model = AcuerdoPago
        fields = ('__all__')


class CuentasPorCobrarSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('id','total_pagar', 'numero_identificacion', 'nombre_deudor', 'cliente',
                  'estado_obligacion', 'fecha_ultimo_pago', 'dias_mora', 'saldo_vencido')
