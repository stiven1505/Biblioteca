# Generated by Django 4.2.6 on 2023-10-06 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaAPP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
