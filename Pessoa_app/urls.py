from django.urls import path,re_path
from .views import ListaContatoView, ListaPessoaView, CriarPessoaView, EditarPessoaView, DeletarPessoaView
from .views import contatos, criar_contato, deletar_contato, editar_contato
from django.contrib.auth.decorators import login_required
#configuração do namespcae
app_name = 'Pessoa_app' #localhost:8000/pessoas/

urlpatterns = [
    path('',login_required(ListaPessoaView.as_view()),name='listapessoaview'),
    path('criarpessoa/',login_required(CriarPessoaView.as_view()),name='criarpessoaview'),
    path('editarpessoa/<slug:pk>/',login_required(EditarPessoaView.as_view()),name='editarpessoaview'),
    path('excluirpessoa/<slug:pk>/',login_required(DeletarPessoaView.as_view()),name='excluirpessoaview'),

    path('listarcontato/<slug:pk_pessoa>/',login_required(contatos),name='listarcontatodef'),
    path('criarcontato/<slug:pk_pessoa>/',login_required(criar_contato),name='criarcontatodef'),
    path('editarcontato/<slug:pk_pessoa>/<slug:pk>',login_required(editar_contato),name='editarcontatodef'),
    path('deletarcontato/<slug:pk_pessoa>/<slug:pk>',login_required(deletar_contato),name='deletarcontatodef'),
]