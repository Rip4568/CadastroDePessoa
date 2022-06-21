from django.contrib import admin
from .models import Contato, Pessoa
# Register your models here.

#registre contato e Pessoa no admin
admin.site.register(Contato)
admin.site.register(Pessoa)