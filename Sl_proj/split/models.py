from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    gname = models.CharField(max_length=40)
    participants = models.ManyToManyField(User)


class GroupTransaction(models.Model):
    owe = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owe')
    ewo = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ewo')
    amount = models.FloatField()
    gname = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.owe) + '-' + str(self.amount) + '-' + str(self.ewo)+'-' + str(self.gname.gname)
