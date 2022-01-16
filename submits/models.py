from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class User(AbstractUser):
    active_class = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile', default='profile/avatar128.png', blank=True)
    RA = models.CharField(max_length=20, blank=False, null=False, default='RA0000')

    def __str__(self):
        return self.username

class Grades(models.Model):
    user_model = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nota = models.FloatField()
    atividade = models.IntegerField()
    
    def __str__(self):
        return f'{self.user_model} = {self.nota}' 
    
class Submission(models.Model):
    user_model = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    atividade = models.IntegerField() # alterar para relação com modelo Atividade
    nota = models.FloatField()
    partial = models.CharField(max_length=500)
    debug_data = models.CharField(max_length=1000)
    submit_time = models.DateField(default=timezone.now)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nota)

class Course(models.Model):
    name = models.CharField(max_length=500)
    student = models.ManyToManyField(User)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    requeriments = models.CharField(max_length=500)
    year = models.IntegerField()
    semester = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()
    inscriptions_open = models.BooleanField()
    youtube = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Atividade(models.Model):
    '''
    Nome
    curso -> models.ForeignKey() onetomany -> Curso
    data_inicio
    data_fim
    descrição
    tags
    recebendo_respostas
    template_modelo
    script_teste
    errata (lista txt)
    gabarito
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    nome = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=500)
    receiving_submissions = models.BooleanField()

