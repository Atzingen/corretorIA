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


class Course(models.Model):
    name = models.CharField(max_length=500)
    user = models.ManyToManyField(User)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000, null=True, blank=True)
    requeriments = models.CharField(max_length=500, null=True, blank=True)
    year = models.IntegerField()
    semester = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()
    subscription_open = models.BooleanField()
    youtube = models.CharField(max_length=100)
    github = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Activity(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=500, null=True)
    receiving_submissions = models.BooleanField()
    template_script = models.FileField(upload_to ='scripts/template_scripts/')
    correction_script = models.FileField(upload_to ='scripts/correction_scripts/')
    perfect_script = models.FileField(upload_to ='scripts/perfect_scripts/')
    errata = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Grades(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, default=1, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return f'{self.user} = {self.score}' 


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, default=1, on_delete=models.CASCADE)
    score = models.FloatField()
    partial = models.CharField(max_length=500)
    debug_data = models.CharField(max_length=1000, null=True, blank=True)
    submit_time = models.DateField(default=timezone.now)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.score)