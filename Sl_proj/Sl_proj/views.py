from django.shortcuts import render


def home(request):
    return render(request, 'Sl_proj/home.html', {})


