from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atividades', views.atividades, name='atividades'),
    path('notas', views.notas, name='notas'),
    path('submit', views.submit, name='submit'),
    path('user_page', views.user_page, name='user_page'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout, name='logout')
]