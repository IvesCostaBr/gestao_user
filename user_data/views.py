from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from .models import UserData
# Create your views here.

class CreateUserData(CreateView):
    model = UserData
    fields = ('nome_completo', 'cpf', 'endereco', 'profile_photo')
    success_url = HttpResponse('Cadastro Realizado')
