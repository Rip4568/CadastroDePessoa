from django.contrib import admin
from .models import Contato, Pessoa
# Register your models here.

@admin.action(description='Ativar Pessoas Selecionadas')
def ativar_todos(modeladmin,request,queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar Pessoas Selecionadas')
def desativar_todos(modeladmin,request,queryset):
    queryset.update(ativa=False)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    #Listar os seguintes campos na tela
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa',
        ]
    #Tipo de filtros para melhor busca
    list_filter = [
        'ativa'
        ]
    #campo de pesquisa para determinado elemento/atributo
    search_fields = [
        'nome_completo'
    ]
    actions = [
        ativar_todos,
        desativar_todos,
    ]

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = [
        'pessoa',
        'tipo',
        'contato',
    ]
    list_filter = [
        'tipo','pessoa'
    ]
    search_fields = [
        'contato',
        'tipo'

    ]