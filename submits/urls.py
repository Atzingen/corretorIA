from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atividades', views.atividades, name='atividades'),
    path('notas', views.notas, name='notas'),
    path("subscribe/<course>", views.subscribe, name="subscribe"),
    path('course/<int:id>', views.course, name='course'),
    path('submit', views.submit, name='submit'),
    path('script_download/<file_name>', views.script_download, name='script_download'),
    path('user_page', views.user_page, name='user_page'),
    path('meus_cursos', views.my_courses, name='meus_cursos'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout, name='logout'),
    path('webhook_6404466046', views.webhook, name='webhook'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]