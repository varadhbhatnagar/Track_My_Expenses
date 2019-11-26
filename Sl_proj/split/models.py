from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Group(models.Model):
    gname = models.CharField(max_length=40)
    participants = models.ManyToManyField(User)
    
    def __str__(self):
        return str(self.gname)

    def get_absolute_url(self):
        return reverse('groups', kwargs={})


class GroupTransaction(models.Model):
    owe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owe')
    ewo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ewo')
    amount = models.FloatField()
    gname = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owe) + '-' + str(self.amount) + '-' + str(self.ewo)+'-' + str(self.gname.gname)
