from django.shortcuts import render


def home(request):
    # PDF functionality removed — render page without PDF context
    return render(request, 'mainapp/index.html')