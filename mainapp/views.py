from django.shortcuts import render
from django.http import JsonResponse
import time


def home(request):
    # render page and provide module indexes for template loop
    modules = list(range(1, 10))  # 1..9
    return render(request, 'mainapp/index.html', {'modules': modules})


def module_status(request):
    # Placeholder API: returns current statuses for 9 modules.
    # Replace this with real MQTT-backed statuses later.
    modules = []
    ts = int(time.time())
    for i in range(1, 10):
        modules.append({'id': i, 'value': '' , 'ts': ts})
    return JsonResponse({'modules': modules})