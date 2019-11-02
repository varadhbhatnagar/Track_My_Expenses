from django.http import Http404
from .models import Transaction
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy, reverse


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


class TransactionCreate(CreateView):
    model = Transaction
    fields = ['details', 'amount', 'category', 'user']

    #This will be used when user login has been added.
    '''
    def form_valid(self, form):
        form.instance.user = self.request.
        return super(TransactionCreate, self).form_valid(form)
    '''


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = ['details', 'amount', 'category', 'user']


class TransactionDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('index')

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