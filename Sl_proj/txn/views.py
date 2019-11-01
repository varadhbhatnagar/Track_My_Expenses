from django.http import Http404
from .models import *
from django.shortcuts import render
from .optimize_transaction import optimize_transaction


def detail(request, user_id):
    my_txn = Transaction.objects.filter(user=user_id)
    if len(my_txn) == 0:
        raise Http404("Invalid User ID")

    context = {'my_txn': my_txn}
    return render(request, 'txn/detail.html', context)


def optimize(request, group_id):
    Transaction_list = GroupTransaction.objects.filter(gname=group_id)
    if len(Transaction_list) == 0:
        raise Http404("Invalid User ID")

    opt=optimize_transaction(Transaction_list)
    fin=opt.resolve()

    return HttpResponse(fin)
