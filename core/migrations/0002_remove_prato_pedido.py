# Generated by Django 4.2.2 on 2023-08-10 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prato',
            name='pedido',
        ),
    ]