from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Cliente, Persona, ObligacionFinanciera, CuentasPorCobrar, AcuerdoPago
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.
# Necesitamos saber como se va a hacer el acoplamiento para la inserción de los datos a nuestra base de datos
class CuentasPorCobrarAdmin(admin.ModelAdmin):
    list_display = ['get_obligacion_cliente', 'get_obligacion_persona', 'saldo_vencido', 'obligacion']
    
    @admin.display(description='Cliente')
    def get_obligacion_cliente(self, obj):
        return obj.obligacion.cliente
    
    @admin.display(description='Deudor')
    def get_obligacion_persona(self, obj):
        return obj.obligacion.persona
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                #mostraremos un mensaje de error si el usuario carga un archivo que no corresponde a un .csv
                messages.warning(request, 'Solo se pueden subir archivos .csv')
                return HttpResponseRedirect(request.path_info)

            #decodificamos a un formato que podamos entender
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            #recorremos una list con cada uno de los capos separados por una coma
            for x in csv_data:
                fields = x.split(",")
                print(fields)
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        #Devolvemos un form de tipo file, el cual renderizaremos en un template llamado csv_upload.html
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data) 
            

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'primer_nombre', 'primer_apellido', 'numero_identificacion', 'email']

class AcuerdoPagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'obligacion', 'valor_cuota', 'fecha_compromiso']

class ObligacionFinancieraAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'numero_referencia']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'url_logo']

class CsvImportForm(forms.Form):
    # Este el formulario que nos da django y que por medio de un parametro label se le pasa el nombre del label
    csv_upload = forms.FileField(label="CARGA ARCHIVO")

#Registramos nustra site
admin.site.register(CuentasPorCobrar, CuentasPorCobrarAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(AcuerdoPago, AcuerdoPagoAdmin)
admin.site.register(ObligacionFinanciera, ObligacionFinancieraAdmin)
admin.site.register(Cliente, ClienteAdmin)
