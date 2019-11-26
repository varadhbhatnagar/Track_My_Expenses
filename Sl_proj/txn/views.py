from django.http import Http404
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse


def crop_ocr(request):
    x1 = request.POST.get('x1')
    x2 = request.POST.get('x2')
    print(x1, x2)
    return HttpResponse("Success")

        
class FileUploadForm(forms.Form):
    file_source = forms.FileField()

def index(request):
    my_txn = Transaction.objects.filter(user=request.user.pk)
    context = {'my_txn': my_txn}
    return render(request, 'txn/index.html', context)


def detail(request, pk):
    txn_detail = get_object_or_404(Transaction, pk=pk)

    if request.user.pk == txn_detail.user.pk:
        context = {'txn_detail': txn_detail}
        return render(request, 'txn/detail.html', context)
    else:
        raise Http404("You can't view this page")


class TransactionCreate(CreateView):
    model = Transaction
    fields = ['bill', 'details', 'amount', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TransactionCreate, self).form_valid(form)


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = ['details', 'amount', 'category', 'bill']


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

