from django.http import Http404
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse, JsonResponse


def crop_ocr(request):
    """!
    @detailed handles AJAX request and applies OCR on image
    @return String amount-detail of the receipts
    """
    x1 = request.POST.get('x1')
    x2 = request.POST.get('x2')
    print(request.POST)
    print(request.FILES)
    print('===')
    print(x1, x2)
    return JsonResponse({'Success':True})

        
class FileUploadForm(forms.Form):
    file_source = forms.FileField()

def index(request):
    """!
    @detailed extracts transaction information of logged in user
    @return path to ledger page along with user transaction details
    """
    my_txn = Transaction.objects.filter(user=request.user.pk)
    context = {'my_txn': my_txn}
    return render(request, 'txn/index.html', context)


def detail(request, pk):
    """!
    @detailed information about particular transaction
    @return complete transaction detail or Error page 
    """
    txn_detail = get_object_or_404(Transaction, pk=pk)

    if request.user.pk == txn_detail.user.pk:
        context = {'txn_detail': txn_detail}
        return render(request, 'txn/detail.html', context)
    else:
        raise Http404("You can't view this page")


class TransactionCreate(CreateView):
    """!
    @detailed creates new entry in transaction table
    """
    model = Transaction
    fields = ['bill', 'details', 'amount', 'category']

    def form_valid(self, form):
        """!
        @detailed validated transaction form """
        form.instance.user = self.request.user
        return super(TransactionCreate, self).form_valid(form)


class TransactionUpdate(UpdateView):
    """!
    @detailed updates pre-existing transaction
    """
    model = Transaction
    fields = ['details', 'amount', 'category', 'bill']


class TransactionDelete(DeleteView):
    """!
    @detailed removes a transaction entry from the table
    """
    model = Transaction
    success_url = reverse_lazy('index')


