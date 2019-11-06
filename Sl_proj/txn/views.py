from django.http import Http404, HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from .forms import UserForm
from .optimize_transaction import optimize_transaction


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


class UserFormView(View):
    form_class = UserForm
    template_name = 'txn/registration_form.html'

    # displays a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index/', args=user.pk)

        return render(request, self.template_name, {'form': form})


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


# def analysis(request, user_id):
#     my_txn = Transaction.objects.filter(user=user_id)
#     temp=[]
    

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
