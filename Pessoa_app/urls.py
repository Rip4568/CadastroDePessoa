from django.urls import path,re_path
from .views import ListaContatoView, ListaPessoaView, CriarPessoaView, EditarPessoaView, DeletarPessoaView
from .views import contatos, criar_contato, deletar_contato, editar_contato
#configuração do namespcae
app_name = 'Pessoa_app' #localhost:8000/pessoas/

urlpatterns = [
    path('',ListaPessoaView.as_view(),name='listapessoaview'),
    path('criarpessoa/',CriarPessoaView.as_view(),name='criarpessoaview'),
    path('editarpessoa/<slug:pk>/',EditarPessoaView.as_view(),name='editarpessoaview'),
    path('excluirpessoa/<slug:pk>/',DeletarPessoaView.as_view(),name='excluirpessoaview'),

    path('listarcontato/<slug:pk_pessoa>/',contatos,name='listarcontatodef'),
    path('criarcontato/<slug:pk_pessoa>/',criar_contato,name='criarcontatodef'),
    path('editarcontato/<slug:pk_pessoa>/<slug:pk>',editar_contato,name='editarcontatodef'),
    path('deletarcontato/<slug:pk_pessoa>/<slug:pk>',deletar_contato,name='deletarcontatodef'),
]