from .optimize_transaction import optimize_transaction
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import GroupTransaction, Group
from Sl_proj.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from txn.models import Transaction

# Create your views here.


def optimize(request, pk):
    Transaction_list = GroupTransaction.objects.filter(gname=pk)
    context = {'group_id': pk}
    if len(Transaction_list) == 0:
        return render(request, 'split/optimized.html', context)

    opt = optimize_transaction(Transaction_list)
    minimized_trans = opt.resolve()

    GroupTransaction.objects.filter(gname=pk).delete()

    for trans in minimized_trans:
        add_trans = GroupTransaction(owe=User.objects.get(pk=trans[2]), ewo=User.objects.get(
            pk=trans[0]), amount=trans[1], gname=Group.objects.get(pk=pk))
        add_trans.save()

    context = {'optimize': GroupTransaction.objects.filter(
        gname=pk), 'group_id': pk}
    return render(request, 'split/optimized.html', context)

def settle(request, pk):
    GroupTransaction.objects.filter(pk=pk).delete()
    return render(request, 'txn/index.html')


def groups(request):
    my_group = Group.objects.filter(participants__pk=request.user.pk)
    context = {'my_group': my_group}
    return render(request, 'split/index.html', context)


class GroupCreate(CreateView):
    model = Group
    fields = ['gname', 'participants']

    def form_valid(self, form):
        return super(GroupCreate, self).form_valid(form)


class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('groups')


class TransCreate(CreateView):
    model = Transaction
    fields = ['details', 'amount', 'category', 'bill']

    def form_valid(self, form, **kwargs):
        group_id = self.kwargs['pk']
        user_list = Group.objects.values('participants').filter(pk=group_id)
        user_id = list(user_list)
        final = {}
        for user in user_id:
            final[list(user.values())[0]] = 1
        total = int(form['amount'].value())
        total_participants = len(user_id)
        category = form['category'].value()
        details = form['details'].value()
        req = total/total_participants
        for user in final.keys():
            add_trans = Transaction(
                details=details, amount=req, category=category, user=User.objects.get(pk=user), bill=None)
            add_trans.save()
        payer = self.request.user.pk
        final.pop(payer)

        for user in final.keys():
            add_trans = GroupTransaction(owe=User.objects.get(pk=user), ewo=User.objects.get(
                pk=payer), amount=req, gname=Group.objects.get(pk=group_id))
            add_trans.save()

        return render(self.request, 'txn/index.html')


