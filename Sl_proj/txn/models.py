from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Transaction(models.Model):
    details = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #bill = models.FilePathField(null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index', kwargs={'user_id': self.user_id})

    def __str__(self):
        return self.details + '-' + str(self.amount)