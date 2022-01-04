# Generated by Django 3.2.5 on 2021-12-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0008_alter_acuerdopago_fecha_compromiso'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.EmailField(default='hectorcohenmaldonado@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='primer_nombre',
            field=models.CharField(max_length=100, verbose_name='primer nombre'),
        ),
    ]