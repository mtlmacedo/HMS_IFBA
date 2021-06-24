from django.contrib import admin
from HotelIFBA.models import Empresa, Cliente, Colaborador, Reserva, Estadia

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

class Reservas(admin.ModelAdmin):
    list_display = ('id', 'dataEntrada', 'dataSaida', 'tipoQuarto', 'qtdPessoas')
    list_display_links = ('id', 'dataEntrada')

class Estadias(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'quarto', 'dataEntrada', 'dataSaida', 'dadosPagamento')
    list_display_links = ('id', 'cliente')


admin.site.register(Empresa, Empresas)
admin.site.register(Cliente, Clientes)
admin.site.register(Colaborador, Colaboradores)
admin.site.register(Reserva, Reservas)
admin.site.register(Estadia, Estadias)