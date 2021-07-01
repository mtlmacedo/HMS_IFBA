from django.contrib import admin
from HotelIFBA.models import *

class Empresas(admin.ModelAdmin):
    list_display = ('id', 'nomeEmpresa', 'proprietario', 'endereco', 'telefone', 'categoria', 'email')
    list_display_links = ('id', 'nomeEmpresa', 'proprietario', 'endereco', 'telefone', 'categoria', 'email')

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nomeCliente', 'data_nascimento', 'email', 'endereco', 'nacionalidade', 'telefone',
     'numero_id', 'data_exp')
    list_display_links = ('id', 'nomeCliente', 'email')

class Colaboradores(admin.ModelAdmin):
    list_display = ('id', 'nomeCompleto', 'cpf', 'login', 'senha', 'cargo')
    list_display_links = ('nomeCompleto', 'cargo', 'senha')

class TipoServicos(admin.ModelAdmin):
    list_display = ('id', 'preco', 'epoca_ano', 'tipo', 'qtd_pessoas')
    list_display_links = ('id', 'preco', 'epoca_ano', 'tipo', 'qtd_pessoas')

class Quartos(admin.ModelAdmin):
    list_display = ('id', 'numeroQuarto', 'andar', 'capacidade', 'disponibilidade')
    list_display_links = ('id', 'numeroQuarto', 'andar', 'capacidade', 'disponibilidade')

class Reservas(admin.ModelAdmin):
    list_display = ('id', 'dataEntrada', 'dataSaida', 'quarto', 'qtd_pessoas', 'cliente', 'servico')
    list_display_links = ('id', 'dataEntrada', 'dataSaida', 'quarto', 'cliente')

class Estadias(admin.ModelAdmin):
    list_display = ('id', 'id', 'cliente', 'dataEntrada', 'dataSaida', 'qtd_pessoas', 'qtd_quartos', 'cliente', 'servico', 'dadosPagamento')
    list_display_links = ('id', 'dataEntrada', 'dataSaida')

class Estatisticas(admin.ModelAdmin):
    list_display = ('id','trimestre','taxaOcupacaoQuartos','taxaQuartosVendidos','faturamentoDoTrimestre','faturamentoAnual','ano','clienteId', 'clientePremium','custoTotalCliente')
    search_fields = ('id','trimestre','taxaOcupacaoQuartos','taxaQuartosVendidos','faturamentoDoTrimestre','faturamentoAnual','ano','clienteId', 'clientePremium','custoTotalCliente')



admin.site.register(Empresa, Empresas)
admin.site.register(Cliente, Clientes)
admin.site.register(Colaborador, Colaboradores)
admin.site.register(Reserva, Reservas)
admin.site.register(Estadia, Estadias)
admin.site.register(Quarto, Quartos)
admin.site.register(TipoServico, TipoServicos)