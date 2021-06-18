from django.contrib import admin
from HotelIFBA.models import Empresa

class Empresas(admin.ModelAdmin):
    list_display = ('nomeEmpresa', 'cnpj')
    list_display_links = ('cnpj', 'nomeEmpresa')
    search_fields = ('nomeEmpresa',)

admin.site.register(Empresa, Empresas)