from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class Profile_info(models.Model):
    user_model = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    active_class = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='static')

    def __str__(self):
        return self.user_model.name

class Notas(models.Model):
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
    