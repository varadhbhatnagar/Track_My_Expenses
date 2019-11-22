from django.shortcuts import render
from django.db.models import Sum
from txn.models import Transaction


# Create your views here.

def analysis(request):
    data = Transaction.objects.filter(user=request.user.pk).values('category').annotate(Sum('amount'))
    # context = dict(zip(data[:, 0], data[:, 1]))
    # return render(request, 'txn/test.html', context)
    dict1 = {}
    value = []
    label = []
    for i in data:
        value.append(i['amount__sum'])
        label.append(i['category'])
    dict1 = {'value': value, 'label': label}
    print(dict1)
    return render(request, 'graphs/analysis.html', dict1)
