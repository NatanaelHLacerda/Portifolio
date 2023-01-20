from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        login = request.POST.get('login')
        #nome = request.POST.get('nome_completo')
        email = request.POST.get('email')
        #celular = request.POST.get('celular')
        #genero = request.POST.get('gender')
        senha = request.POST.get('senha')
        
        # confirmar_senha = request.POST.get('confirmar_senha')

        '''if len(primeiro_nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os dados!')
            return render(request, 'cadastro.html')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não conferem!')
            return render(request, 'cadastro.html')'''
        try:
            user = User.objects.create_user(username=login, email=email, password=senha)
            #messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            
        except:
            return HttpResponse('Deu erro aqui')
            messages.add_message(request, constants.WARNING, 'Usuário já existente')
            return render(request, 'cadastro.html')


def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username=nome, password=senha)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Login ou senha inválido.')
            return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('/auth/login')

