# Generated by Django 2.2.5 on 2019-11-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txn', '0003_transaction_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bill',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
