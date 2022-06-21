from django.http import Http404,HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contato, Pessoa
from .forms import PessoaForm
# Create your views here.
#por padrão as classes instanciadas de views.generic já esperam que exista um template dentro da pasta do app
#para ser chamada como o nome da classe, porém, se você quiser que o nome do template seja diferente, você pode passar o nome do template como segundo parâmetro
#examplo: ListaPessoaView.as_view(template_name='pessoa_app/lista_pessoa.html')
class ListaPessoaView(ListView):
    model = Pessoa
    #essa consulta (queryset) ira retornar uma variavel chamda object_list, a qual podera ser usada no template
    queryset = Pessoa.objects.all().order_by('nome_completo')

    def get_queryset(self):#esse metodo é chamado automaticamente quando a view for chamada
        query_set = super().get_queryset()#retorna o queryset do pai
        filtro_nome = self.request.GET.get('nome-buscar') or ''#retorna o valor do campo nome-buscar ou '' se não existir
        
        if filtro_nome:#se o valor do campo nome-buscar for diferente de None
            query_set = query_set.filter(nome_completo__icontains=filtro_nome)
        
        return query_set.filter(nome_completo__icontains=filtro_nome)#filtra o queryset com o valor do campo nome-buscar

class CriarPessoaView(CreateView):
    model = Pessoa #modelo que será usado para criar o objeto, aqui não é necessario passar o modelo, pois o modelo já é passado pelo form
    form_class = PessoaForm #formulario que será usado para criar o objeto
    success_url = '/pessoas/' #url que será redirecionada após o sucesso da criação do objeto

class EditarPessoaView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/' #url que será redirecionada após o sucesso da criação do objeto
    #esse parâmetro é necessário para que o django possa identificar qual objeto será editado
    #o django ira buscar o objeto com o id passado como parâmetro na url
    #exemplo: /pessoas/1/editar/
    #o django ira buscar o objeto com o id 1 e ira preencher o formulario com os dados do objeto

class DeletarPessoaView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'

class ListaContatoView(ListView):
    model = Contato
    queryset = Contato.objects.all().order_by('contato')


def contatos(request,pk):
    contatos = Contato.objects.filter(pessoa=pk)
    pessoa = Pessoa.objects.get(pk=pk)
    return render(request,'contato/contato_list.html',{'contatos':contatos,'pessoa':pessoa})
    #return render(request,'Pessoa_app/pessoa_list.html',{'contatos':contatos,'pessoa':pessoa})