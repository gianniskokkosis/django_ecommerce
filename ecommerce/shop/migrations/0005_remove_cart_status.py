# Generated by Django 3.1.6 on 2021-02-28 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201013_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]
