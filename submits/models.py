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
    
class Submission(models.Model):
    user_model = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    atividade = models.IntegerField()
    nota = models.FloatField()
    partial = models.CharField(max_length=500)
    debug_data = models.CharField(max_length=1000)
    submit_time = models.DateField(default=timezone.now)
    is_valid = models.BooleanField(default=False)
