from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration', views.registration, name='registration'),
    path('test', views.test, name='test'),
    path('result', views.result, name='result')
]
