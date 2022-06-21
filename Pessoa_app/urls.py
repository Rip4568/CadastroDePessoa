from django.urls import path,re_path
from .views import ListaContatoView, ListaPessoaView, CriarPessoaView, EditarPessoaView, DeletarPessoaView, contatos

#configuração do namespcae
app_name = 'Pessoa_app'

urlpatterns = [
    path('',ListaPessoaView.as_view(),name='listapessoaview'),
    path('criarpessoa/',CriarPessoaView.as_view(),name='criarpessoaview'),
    path('editarpessoa/<slug:pk>',EditarPessoaView.as_view(),name='editarpessoaview'),
    path('excluirpessoa/<slug:pk>',DeletarPessoaView.as_view(),name='excluirpessoaview'),
    path('listarcontato/<slug:pk>',contatos,name='listarcontatoview'),
]