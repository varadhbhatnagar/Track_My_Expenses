from django.shortcuts import render,HttpResponse
from txn.models import *


def index(request):
    return render(request, 'Sl_proj/index.html', {})
