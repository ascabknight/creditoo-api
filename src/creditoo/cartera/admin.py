from django.contrib import admin
from .models import Cliente, Persona
from .models import ObligacionFinanciera, CuentasPorCobrar

# Register your models here.
admin.site.register(Persona)
admin.site.register(ObligacionFinanciera)
admin.site.register(Cliente)

class CuentasPorCobrarAdmin(admin.ModelAdmin):
    list_display = ['get_obligacion_cliente', 'get_obligacion_persona', 'saldo_vencido']
    
    @admin.display(description='Cliente')
    def get_obligacion_cliente(self, obj):
        return obj.obligacion.cliente
    
    @admin.display(description='Deudor')
    def get_obligacion_persona(self, obj):
        return obj.obligacion.persona


admin.site.register(CuentasPorCobrar, CuentasPorCobrarAdmin)