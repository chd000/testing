from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('list', views.quest_list, name='list'),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration', views.registration, name='registration'),
    path('test', views.test, name='test'),
]