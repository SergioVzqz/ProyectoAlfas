# Generated by Django 3.0.6 on 2020-05-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20200520_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pais',
            field=models.CharField(choices=[('MX', 'Mexico'), ('EU', 'Estados Unidos')], default='Mexico', max_length=20),
        ),
    ]
