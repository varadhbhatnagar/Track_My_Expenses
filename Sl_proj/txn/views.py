from django.http import Http404
from .models import Transaction
from django.shortcuts import render, get_object_or_404
from django.views import generic


def index(request, user_id):
    my_txn = Transaction.objects.filter(user=user_id)
    if len(my_txn) == 0:
        raise Http404("Invalid User ID")

    context = {'my_txn': my_txn}
    return render(request, 'txn/index.html', context)


def detail(request, pk):
    txn_detail = get_object_or_404(Transaction, pk=pk)
    context = {'txn_detail': txn_detail}
    return render(request, 'txn/detail.html', context)

# Generic View Implementation. May be useful later.
'''
class IndexView(generic.ListView):
    template_name = 'txn/detail.html'
    context_object_name = 'my_txn'

    def get_queryset(self):
        return Transaction.objects.filter()


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'txn/detail.html'
'''