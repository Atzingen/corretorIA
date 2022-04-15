from django.contrib import admin

# Register your models here.
from .models import User, Course, Activity, Grades, Submission

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Activity)
admin.site.register(Grades)
admin.site.register(Submission)