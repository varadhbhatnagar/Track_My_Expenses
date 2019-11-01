from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    details = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #bill = models.FilePathField(null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.details + '-' + str(self.amount)


class Group(models.Model):
    gname = models.CharField(max_length=40)
    participants = models.ManyToManyField(User)


class GroupTransaction(models.Model):
    owe = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owe')
    ewo = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ewo')
    amount = models.FloatField()
    gname = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.owe) + '-' + str(self.amount) + '-' + str(self.ewo)
