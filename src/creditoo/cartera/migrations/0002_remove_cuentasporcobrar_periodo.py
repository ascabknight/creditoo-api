# Generated by Django 3.2.5 on 2022-03-23 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentasporcobrar',
            name='periodo',
        ),
    ]
