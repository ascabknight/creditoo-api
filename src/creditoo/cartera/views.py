from urllib.parse import quote_from_bytes
from rest_framework import viewsets

from .serializers import PersonaSerializer, CuentasPorCobrarSerializer, AcuerdoPagoSerializer, ObligacionFinancieraSerializer, EstudioCreditoSerializer
from .models import AcuerdoPago, EstudioCredito, ObligacionFinanciera, Persona, CuentasPorCobrar

# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = AcuerdoPago.objects.all()

    def get_queryset(self):
        queryset = Persona.objects.all()
        usuario = self.request.query_params.get('usuario')
        if usuario is not None:
            queryset = queryset.filter(
                numero_identificacion=usuario)
        return queryset

    def create(self, request):
        data = request.data
        return super().create(request)


class ObligacionFinancieraViewSet(viewsets.ModelViewSet):
    queryset = ObligacionFinanciera.objects.all()
    serializer_class = ObligacionFinancieraSerializer


class AcuerdoPagoViewSet(viewsets.ModelViewSet):
    serializer_class = AcuerdoPagoSerializer
    queryset = AcuerdoPago.objects.all()

    def get_queryset(self):
        queryset = AcuerdoPago.objects.all()
        usuario = self.request.query_params.get('usuario')
        if usuario is not None:
            queryset = queryset.filter(
                obligacion=usuario)
        return queryset

    def create(self, request):
        data = request.data
        return super().create(request)


class EstudioCreditoViewSet(viewsets.ModelViewSet):
    queryset = EstudioCredito.objects.all()
    serializer_class = EstudioCreditoSerializer


class CuentasPorCobrarViewSet(viewsets.ModelViewSet):
    serializer_class = CuentasPorCobrarSerializer

    def get_queryset(self):
        queryset = CuentasPorCobrar.objects.all()
        usuario = self.request.query_params.get('usuario')
        if usuario is not None:
            queryset = queryset.filter(
                obligacion__persona__numero_identificacion=usuario)
        return queryset
