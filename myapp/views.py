from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>哈囉！這是我的第一個 Django 網頁！</h1>")