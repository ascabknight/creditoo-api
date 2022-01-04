from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import renderer_classes

from .serializers import PersonaSerializer, CuentasPorCobrarSerializer
from .models import Persona, CuentasPorCobrar

# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class CuentasPorCobrarViewSet(viewsets.ModelViewSet):
    serializer_class = CuentasPorCobrarSerializer

    def get_queryset(self):
        queryset = CuentasPorCobrar.objects.all()
        usuario = self.request.query_params.get('usuario')
        if usuario is not None:
            queryset = queryset.filter(obligacion__persona__numero_identificacion=usuario)
        return queryset

