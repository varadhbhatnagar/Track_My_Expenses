from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORY_CHOICES = (('Food', 'Food'), ('Shopping', 'Shopping'), ('Health and Fitness', 'Health and Fitness'), ('Entertainment', 'Entertainment'), ('Travel', 'Travel'), ('Rent', 'Rent'), ('Gifts', 'Gifts'), ('Other', 'Other'))


class Transaction(models.Model):
    details = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=18, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    bill = models.FileField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index', kwargs={})

    def __str__(self):
        return self.details + '-' + str(self.amount)
