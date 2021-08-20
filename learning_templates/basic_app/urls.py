from django import urls
from django.urls import path
from basic_app import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('relative', views.relative, name='relative_url_template'),
    path('base', views.base, name='base'),
    path('user_login', views.user_login, name='user_login'),
]
