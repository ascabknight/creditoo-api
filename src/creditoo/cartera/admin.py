from django.contrib import admin
from .models import *

# Register your models here.
class CuentasPorCobrarAdmin(admin.ModelAdmin):
    list_display = ['get_obligacion_cliente', 'get_obligacion_persona', 'saldo_vencido']
    
    @admin.display(description='Cliente')
    def get_obligacion_cliente(self, obj):
        return obj.obligacion.cliente
    
    @admin.display(description='Deudor')
    def get_obligacion_persona(self, obj):
        return obj.obligacion.persona
    
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_completo', 'email', 'numero_identificacion']

class AcuerdoPagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'obligacion', 'valor_cuota', 'fecha_compromiso']
    
class ObligacionFinancieraAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'numero_referencia']
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'url_logo']

# Register your models here.
class EstudioCreditoAdmin(admin.ModelAdmin):
    list_display = ['persona', 'id', 'documento_adjunto']

admin.site.register(CuentasPorCobrar, CuentasPorCobrarAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(AcuerdoPago, AcuerdoPagoAdmin)
admin.site.register(ObligacionFinanciera, ObligacionFinancieraAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(EstudioCredito, EstudioCreditoAdmin)