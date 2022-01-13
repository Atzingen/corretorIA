from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atividades', views.atividades, name='atividades'),
    path('notas', views.notas, name='notas'),
    path('submit', views.submit, name='submit'),
    path('user_page', views.user_page, name='user_page'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout, name='logout'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]