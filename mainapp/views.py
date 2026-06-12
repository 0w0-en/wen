from django.shortcuts import render
import os
import json


def home(request):
    # try to load extracted PDF data if present
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'static', 'mainapp', 'pdf_extracted.json')
    pdf_data = {}
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            pdf_data = json.load(f)
    except Exception:
        pdf_data = {}
    # check if the static PDF file exists on this host
    pdf_filename = '物聯網最終提案.pdf'
    pdf_static_path = os.path.join(base_dir, 'static', 'mainapp', pdf_filename)
    pdf_exists = os.path.exists(pdf_static_path)

    context = {
        'pdf_summary': pdf_data.get('summary', ''),
        'pdf_headings': pdf_data.get('headings', []),
        'pdf_exists': pdf_exists,
        'pdf_filename': pdf_filename,
    }
    return render(request, 'mainapp/index.html', context)