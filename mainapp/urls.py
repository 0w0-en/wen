# mainapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/module_status/', views.module_status, name='module_status'),
]