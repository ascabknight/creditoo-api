from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PersonaSerializer
from .models import Persona

# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
