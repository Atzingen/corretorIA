from django.contrib import admin

# Register your models here.
from .models import User, Grades, Submission

admin.site.register(User)
admin.site.register(Grades)
admin.site.register(Submission)