from django.http import Http404, HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .optimize_transaction import optimize_transaction
from django.db.models import Sum


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
    fields = ['details', 'amount', 'category', 'user', 'bill']

    # This will be used when user login has been added.
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


def optimize(request, group_id):
    Transaction_list = GroupTransaction.objects.filter(gname=group_id)
    if len(Transaction_list) == 0:
        raise Http404("Invalid User ID")

    opt = optimize_transaction(Transaction_list)
    minimized_trans = opt.resolve()

    GroupTransaction.objects.filter(gname=group_id).delete()

    for trans in minimized_trans:
        add_trans = GroupTransaction(owe=User.objects.get(pk=trans[2]), ewo=User.objects.get(
            pk=trans[0]), amount=trans[1], gname=Group.objects.get(pk=group_id))
        add_trans.save()

    return HttpResponse(GroupTransaction.objects.filter(gname=group_id))


def analysis(request, user_id):
    data=Transaction.objects.filter(user=user_id).values('category').annotate(Sum('amount'))
    # context = dict(zip(data[:, 0], data[:, 1]))
    # return render(request, 'txn/test.html', context)
    dict1={}
    value = []
    label = []
    for i in data:
        value.append(i['amount__sum'])
        label.append(i['category'])
    dict1 = {'value' : value, 'label' : label}
    print(dict1)
    return render(request, 'txn/test.html', dict1)
    

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
