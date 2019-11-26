from django.shortcuts import render
from django.db.models import Sum
from txn.models import Transaction


# Create your views here.

def analysis(request):
    """
    extract the information of logged in user and calculate its 
    expenditure in each domain
    """
    data = Transaction.objects.filter(user=request.user.pk).values('category').annotate(Sum('amount'))
    dict1 = {}
    value = []
    label = []
    for i in data:
        value.append(i['amount__sum'])
        label.append(i['category'])
    dict1 = {'value': value, 'label': label}
    print(dict1)
    return render(request, 'graphs/analysis.html', dict1)
