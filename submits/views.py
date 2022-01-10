from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import RegisterForm, User

def home(request):
    return render(request, 'home.html')

def atividades(request):
    return render(request, 'atividades.html')

def notas(request):
    return render(request, 'notas.html')

@login_required(login_url='login')
def submit(request):
    return render(request, 'submit.html')

def user_page(request):
    if request.method == 'POST':
        post = request.POST
        user = User.objects.get(id=request.user.id)
        user.first_name = post['first_name_update']
        user.last_name = post['last_name_update']
        # user.username = post['username_update']
        user.email = post['email_update']
        user.save()
    return render(request, 'user_page.html')

def registrar(request):
    if request.user.is_authenticated:
        messages.success(request, 'Você já está Registrado')
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            print('is valid !')
            form.save()
            messages.success(request, 'Registro efetuado com sucesso !')
            return redirect('home')
        else:
            messages.success(request, 'Erro no preenchimento do formulário')
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'registrar.html', context)

def login_page(request):
    if request.user.is_authenticated:
        messages.success(request, 'Você já está logado')
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso !')
            return redirect('home')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logoff efetuado')
        return render(request, 'home.html')
    messages.success(request, 'Você ainda não fez Login')
    return redirect('login')
    