from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contato, Pessoa
from .forms import ContatoForm, PessoaForm
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
        query_set = query_set.filter(usuario=self.request.user)#filtrar todas as pessoas com o usuario que criou
        filtro_nome = self.request.GET.get('nome-buscar') or ''#retorna o valor do campo nome-buscar ou '' se não existir
        
        if filtro_nome:#se o valor do campo nome-buscar for diferente de None
            query_set = query_set.filter(nome_completo__icontains=filtro_nome)#filtra o queryset com o valor do campo nome-buscar
        
        return query_set

class CriarPessoaView(CreateView):
    model = Pessoa #modelo que será usado para criar o objeto, aqui não é necessario passar o modelo, pois o modelo já é passado pelo form
    form_class = PessoaForm #formulario que será usado para criar o objeto
    success_url = '/pessoas/' #url que será redirecionada após o sucesso da criação do objeto
    
    #agora precisamos garantir que o formulario seja vinculado ao usuario logado
    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

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
    #def get(self,pk,request)
    #code ...
    model = Contato
    queryset = Contato.objects.all().order_by('contato')

class ContatoDetailView(DetailView):
    model = Contato
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #from django.utils import timezone
        #context['now'] = timezone.now
        return context
    


def contatos(request,pk_pessoa):
    contatos = Contato.objects.filter(pessoa_id=pk_pessoa)
    return render(request,'contato/contato_list.html',{'contatos':contatos,'pk_pessoa':pk_pessoa})
    #return render(request,'Pessoa_app/pessoa_list.html',{'contatos':contatos,'pessoa':pessoa})

def criar_contato(request,pk_pessoa):
    form = ContatoForm()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)#commit false = não registrar no banco de dados
            contato.pessoa_id = pk_pessoa#o campo pessoa_id é o mesmo que esta no banco de dados
            contato.save()
            return redirect(reverse('Pessoa_app:listarcontatodef',args={pk_pessoa}))
            return HttpResponseRedirect('Pessoa_app:listarcontatodef',args={pk_pessoa})
    return render(request,'contato/contato_form.html',{'form':form,'pk_pessoa':pk_pessoa})

def editar_contato(request,pk_pessoa,pk):
    contato = get_object_or_404(Contato,pk=pk)
    form = ContatoForm(instance=contato)#preencher os campos com o objeto contato
    if request.method == 'POST':
        form = ContatoForm(request.POST,instance=contato)
        if form.is_valid():
            form.save()
            return redirect(reverse('Pessoa_app:listarcontatodef',args=[pk_pessoa]))
    return render(request,'contato/contato_form.html',{'form':form})

def deletar_contato(request,pk_pessoa,pk):
    contato = get_object_or_404(Contato,pk=pk)
    contato.delete()
    return redirect(reverse('Pessoa_app:listarcontatodef',args=[pk_pessoa]))

