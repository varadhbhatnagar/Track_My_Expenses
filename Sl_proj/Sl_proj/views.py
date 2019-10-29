from django.shortcuts import render


def index(request):
    return render(request, 'Sl_proj/index.html', {})

