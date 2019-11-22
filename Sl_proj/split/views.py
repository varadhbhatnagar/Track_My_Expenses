from .optimize_transaction import optimize_transaction
from django.http import Http404, HttpResponse
from .models import GroupTransaction, Group
from Sl_proj.models import User
# Create your views here.


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
