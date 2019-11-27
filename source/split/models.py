from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Group(models.Model):
    """!
    Defines the structure of the table used for storing Group
    """
    gname = models.CharField(max_length=40)
    participants = models.ManyToManyField(User)

    def __str__(self):
        """!
        @detailed function which returns summary for a particular Group
        @return String Group name
        """
        return str(self.gname)

    def get_absolute_url(self):
        """!
        @detailed function which redirects to Group page
        @return path to Group page
        """
        return reverse('groups', kwargs={})


class GroupTransaction(models.Model):
    """!
    Defines the structure of the table used for storing GroupTransaction
    """
    owe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owe')
    ewo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ewo')
    amount = models.FloatField()
    gname = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        """!
        @detailed function which returns summary for a transaction in a Group
        @return String Borrower-Amount-Lender-Group Name
        """
        return str(self.owe) + '-' + str(self.amount) + '-' + str(self.ewo)+'-' + str(self.gname.gname)
