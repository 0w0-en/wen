from django.shortcuts import render

# mainapp/views.py
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Django")