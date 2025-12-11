from django.contrib import admin
from .models import Client
from .models import Avaliacao


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'criado_por', 'criado_em')
    search_fields = ('nome', 'email')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('client', 'avaliador', 'criado_em', 'aprovado')
    list_filter = ('aprovado', 'criado_em')
    search_fields = ('client__nome', 'avaliador__username')
