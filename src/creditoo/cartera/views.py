from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PersonaSerializer, CuentasPorCobrarSerializer
from .models import Persona, CuentasPorCobrar

# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class CuentasPorCobrarViewSet(viewsets.ModelViewSet):
    queryset = CuentasPorCobrar.objects.all()
    serializer_class = CuentasPorCobrarSerializer
