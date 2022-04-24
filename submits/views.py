import os, time
import hmac, hashlib
import threading
from multiprocessing import context
from importlib import import_module
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import mimetypes

from submits.corretor import run_tests
from submits.corretor.correction_scripts import test_functions

from submits.models import *
from .forms import RegisterForm, User, UpdataUserForm
from .corretor import utils
from .corretor import correction_scripts

def home(request):
    dados =  list(Course.objects.all().values('name', 'id', 'short_description', 'long_description', 'subscription_open', 
                                         'active', 'start_date', 'end_date', 'youtube', 'github').order_by('-subscription_open', 'start_date'))
    context = {'dados': dados}
    return render(request, 'home.html', context)

def subscribe(request, course):
    messages.success(request, 'Inscrição efetuada !')
    return redirect('home')

def course(request, id):
    dados = Course.objects.filter(id=id).values('name', 'id', 'short_description', 
                   'long_description', 'subscription_open', 'active', 'start_date', 
                   'end_date', 'youtube', 'github').order_by('-subscription_open', 
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
    context = {
        'active': active_activities,
        'inactive': inactive_activities
    }
    return render(request, 'atividades.html', context=context)

@login_required(login_url='login')
def script_download(request, file_name, *args, **kwargs):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\static\\images\\scripts\\template_scripts\\template_atv1_2022_05N9e8J.py' #+ file_name.split('/')[-1]
    path = open(filepath, 'r', encoding='utf-8')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response

@login_required(login_url='login')
def notas(request):
    courses_list = Course.objects.filter(user=request.user)
    activities_list = []
    best_score = []
    score_info = {}
    for course in courses_list:
        activities_list.append(Activity.objects.filter(course=course))
        score_info[course.name] = {}
        for activitie in activities_list[-1]:
            best_score.append(Submission.objects.filter(activity=activitie, user=request.user).aggregate(Max("score")))
            score_info[course.name][activitie.name] = Submission.objects.filter(activity=activitie, user=request.user).aggregate(Max("score"))
    return render(request, 'notas.html', context={'data':score_info})

@login_required
def submit(request):
    if request.method == 'POST' and request.FILES['file']:
        script = request.FILES['file']
        fs = FileSystemStorage(location='submits/corretor/submit_scripts')
        filename = fs.save(script.name.replace('.py', '') + utils.make_salt(16) + '.py', script)
        request.session['submited_file'] = filename
    elif 'process_script' in request.GET:
        module = import_module('submits.corretor.submit_scripts.' + request.session['submited_file'].strip('.py'))
        response = StreamingHttpResponse(test_functions.test_all(module, request.user), status=200, content_type='text/event-stream')
        return response
    return render(request, 'submit.html')

@login_required(login_url='login')
def user_page(request):
    if request.method == 'POST':
        form = UpdataUserForm(request.POST, request.FILES, instance=request.user)
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
    
@csrf_exempt
def webhook(request):
    print('webhook request arrived')
    print(request)
    threading.Thread(target=lambda: [time.sleep(4), os.system('sudo systemctl restart django.service')]).start()
    # sig_header = 'X-Hub-Signature-256'
    # if sig_header in request.headers:
    #     header_splitted = request.headers[sig_header].split("=")
    #     if len(header_splitted) == 2:
    #         req_sign = header_splitted[1]
    #         computed_sign = hmac.new(os.environ.get('GIT_WEBHOOK').encode(), request.data, hashlib.sha256).hexdigest()
    #         if hmac.compare_digest(req_sign, computed_sign):
    #             print("new version, rebooting now")
            #     if app.debug:
            #         threading.Thread(target=lambda: [time.sleep(4), os._exit(-1)]).start() 
            #     else:
            #         threading.Thread(target=lambda: [time.sleep(4), os.system('sudo systemctl restart django.service')]).start()
            # else:
            #     return 'secret did not match'
    return "ok"   