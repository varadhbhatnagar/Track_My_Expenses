# Generated by Django 2.2.6 on 2019-11-01 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('txn', '0005_auto_20191101_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupa',
            name='participants',
        ),
    ]