from django.shortcuts import render
import os
import json


def home(request):
    # try to load extracted PDF data if present
    json_path = os.path.join(os.path.dirname(__file__), 'static', 'mainapp', 'pdf_extracted.json')
    pdf_data = {}
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            pdf_data = json.load(f)
    except Exception:
        pdf_data = {}

    context = {
        'pdf_summary': pdf_data.get('summary', ''),
        'pdf_headings': pdf_data.get('headings', []),
    }
    return render(request, 'mainapp/index.html', context)