# Generated by Django 3.0.8 on 2020-10-13 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201013_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='cart',
        ),
        migrations.AddField(
            model_name='invoice',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
