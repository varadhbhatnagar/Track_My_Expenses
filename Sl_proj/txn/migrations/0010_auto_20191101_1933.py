# Generated by Django 2.2.6 on 2019-11-01 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('txn', '0009_grouptransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouptransaction',
            name='gname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='txn.Group'),
        ),
    ]
