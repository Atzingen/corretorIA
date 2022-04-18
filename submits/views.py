from multiprocessing import context
from re import A
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.storage import FileSystemStorage

from submits.models import *
from .forms import RegisterForm, User, UpdataUserForm
from .corretor import utils

def home(request):
    dados =  list(Course.objects.all().values('name', 'id', 'short_description', 'long_description', 'inscriptions_open', 
                                         'active', 'start_date', 'end_date', 'youtube', 'github').order_by('-inscriptions_open', 'start_date'))
    context = {'dados': dados}
    return render(request, 'home.html', context)

def course(request, id):
    dados = Course.objects.filter(id=id).values('name', 'id', 'short_description', 
                   'long_description', 'inscriptions_open', 'active', 'start_date', 
                   'end_date', 'youtube', 'github').order_by('-inscriptions_open', 
                   'start_date')[0]
    videos_data = utils.list_videos(dados['youtube'].split('=')[-1])
    dados['videos_data'] = videos_data
    context = {'dados': dados}
    return render(request, 'course.html', context)

@login_required(login_url='login')
def atividades(request):
    ids_activities_receiving_submissions = list(request.user.course_set.filter(activity__receiving_submissions=True).values(
        "activity__id").values_list("activity__id", flat=True))
    ids_activities_notreceiving_submissions = list(request.user.course_set.filter(activity__receiving_submissions=False).values(
        "activity__id").values_list("activity__id", flat=True))
    active_activities = Activity.objects.filter(id__in=ids_activities_receiving_submissions)
    inactive_activities = Activity.objects.filter(id__in=ids_activities_notreceiving_submissions)
    print(active_activities)
    print(inactive_activities)
    context = {
        'active': active_activities,
        'inactive': inactive_activities
    }
    return render(request, 'atividades.html', context=context)

@login_required(login_url='login')
def script_templates(request, template_name):
    print(template_name)
    # return the py file: https://fedingo.com/how-to-download-file-in-django/
    return render(request, 'notas.html')

@login_required(login_url='login')
def notas(request):
    return render(request, 'notas.html')

# @login_required(login_url='login')
def submit(request):
    if request.method == 'POST' and request.FILES['file']:
        script = request.FILES['file']
        fs = FileSystemStorage(location='static/scripts')
        filename = fs.save(script.name.replace('.py', '') + utils.make_salt(16) + '.py', script)
        request.session['submited_file'] = filename
    elif 'process_script' in request.GET:
        print(request.GET)
        response = StreamingHttpResponse(utils.hello(), status=200, content_type='text/event-stream')
        return response
    return render(request, 'submit.html')

@login_required(login_url='login')
def user_page(request):
    if request.method == 'POST':
        form = UpdataUserForm(request.POST, request.FILES, instance=request.user)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.info(request, 'Perfil atualizado com sucesso')
        else:
            messages.error(request, 'Erro ao atualizar o perfil')
    return render(request, 'user_page.html')

def registrar(request):
    if request.user.is_authenticated:
        messages.info(request, 'Você já está Registrado')
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Registro efetuado com sucesso !')
            return redirect('home')
        else:
            messages.info(request, 'Erro no preenchimento do formulário')
            context = {'form': form}
            return render(request, 'registrar.html', context)
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'registrar.html', context)

def login_page(request):
    if request.user.is_authenticated:
        messages.info(request, 'Você já está logado')
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, 'Login efetuado com sucesso !')
            return redirect('home')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Logoff efetuado')
    return redirect('home')
    