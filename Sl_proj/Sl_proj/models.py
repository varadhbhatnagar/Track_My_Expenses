from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """!
    @detailed Defines the structure of the table used for storing User Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Annual_Income = models.FloatField(null=True, blank=True)
    Mobile_Number = models.CharField(max_length=10)
    Profile_Picture = models.FileField(blank=True)
