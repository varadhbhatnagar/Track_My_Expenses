# Generated by Django 2.2.5 on 2019-11-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txn', '0005_group_grouptransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='bill',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]