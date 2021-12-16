from rest_framework import serializers

from .models import Persona, CuentasPorCobrar

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','primer_nombre', 'primer_apellido','tipo_identification', 'numero_identificacion')

class CuentasPorCobrarSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('numero_identificacion','nombre_deudor', 'cliente','estado_obligacion', 'fecha_ultimo_pago','dias_mora', 'saldo_vencido')