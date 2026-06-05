from django.shortcuts import render

# mainapp/views.py
from django.http import HttpResponse


def home(request):
    return render(request, 'mainapp/index.html')