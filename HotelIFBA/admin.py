from django.contrib import admin
from HotelIFBA.models import Empresa, Cliente, Colaborador

class Empresas(admin.ModelAdmin):
    list_display = ('nomeEmpresa', 'cnpj')
    list_display_links = ('cnpj', 'nomeEmpresa')
    search_fields = ('nomeEmpresa',)

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nomeCliente', 'dtNascimento')
    list_display_links = ('id', 'nomeCliente')

class Colaboradores(admin.ModelAdmin):
    list_display = ('id', 'nomeCompleto', 'rg')
    list_display_links = ('id', 'nomeCompleto')


admin.site.register(Empresa, Empresas)
admin.site.register(Cliente, Clientes)
admin.site.register(Colaborador, Colaboradores)