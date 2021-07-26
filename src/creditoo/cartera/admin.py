from django.contrib import admin
from .models import Cliente, Persona
from .models import ObligacionFinanciera

# Register your models here.
admin.site.register(Persona)
admin.site.register(ObligacionFinanciera)
admin.site.register(Cliente)