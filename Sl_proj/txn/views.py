from django.http import Http404
from .models import Transaction
from django.shortcuts import render


def detail(request, user_id):
    my_txn = Transaction.objects.filter(user=user_id)
    if len(my_txn) == 0:
        raise Http404("Invalid User ID")

    context = {'my_txn': my_txn}
    return render(request, 'txn/detail.html', context)