from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,FormView,CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'Main_app/index.html'#template que será renderizado


class RegisterView(CreateView):#Classe para criar conta de usuario
    form_class = UserCreationForm
    template_name = 'Main_app/registrar.html'
    success_url = '/pessoas'
    

class ChangeUserView(CreateView):#Classe para alterar formulario do usuario
    form_class = UserChangeForm
    success_url = '/login'
    template_name = 'Main_app/changeform.html'

