from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import renderer_classes

from .serializers import PersonaSerializer, CuentasPorCobrarSerializer, AcuerdoPagoSerializer
from .models import Persona, CuentasPorCobrar, AcuerdoPago

# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class AcuerdoPagoViewSet(viewsets.ModelViewSet):
    serializer_class = AcuerdoPagoSerializer
    queryset = AcuerdoPago.objects.all()

    def create(self, request):
        data = request.data
        return super().create(request)


class CuentasPorCobrarViewSet(viewsets.ModelViewSet):
    serializer_class = CuentasPorCobrarSerializer

    def get_queryset(self):
        queryset = CuentasPorCobrar.objects.all()
        usuario = self.request.query_params.get('usuario')
        print(usuario)
        if usuario is not None:
            queryset = queryset.filter(
                obligacion__persona__identificacion=usuario)
        return queryset
