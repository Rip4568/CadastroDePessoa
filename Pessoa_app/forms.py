from django import forms
from .models import Pessoa, Contato

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(#widget=forms.DateInput(format='%d/%m/%Y'))
    widget=forms.TextInput(attrs={'type':'date'}),)
    class Meta:
        model = Pessoa
        #acredito que esssa é a melhor maneira de lidar com campos a quais você quer ou não ser preenchidos no form
        fields = ['nome_completo','data_nascimento','ativa']


class ContatoForm(forms.ModelForm):
    #configurações da classe aqui
    class Meta:
        model = Contato
        fields = ['tipo','contato']
